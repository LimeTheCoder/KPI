from pymongo.mongo_client import MongoClient
from bson.objectid import ObjectId
from bson.son import SON
from bson.code import Code
import pymongo
import redis
from bson import json_util
from entities import Survey, Doctor

client = MongoClient()
db = client.labDb

redis_client = redis.StrictRedis()
page_size = 50
cnt_key = 'doctor_cnt'


def get_doctor_list(page):
    cnt = redis_client.get(cnt_key)
    if not cnt:
        cnt = db.doctors.find().count()
        redis_client.set(cnt_key, cnt)

    cnt = int(cnt)
    has_next = (cnt > (page * page_size))
    has_prev = (page > 1)

    key = 'doctor:' + str(page)
    data = redis_client.get(key)

    if data:
        print 'Loaded from cache'
        return [Doctor(x) for x in json_util.loads(data)], \
               has_prev, has_next

    data = db.doctors.find().sort('_id', pymongo.ASCENDING).skip((page - 1) * page_size).limit(page_size)
    data = list(data)

    page_max_key = "page_max_obj:" + str(page)
    page_max_obj = str(data[-1]['_id'])

    redis_client.set(page_max_key, page_max_obj)
    redis_client.set(key, json_util.dumps(data))

    print cnt

    print 'Loaded from database'

    return [Doctor(x) for x in data], has_prev, has_next


def get_survey_list():
    cursor = db.surveys.find()
    return [Survey(x) for x in cursor]


def insert_doctor(doctor):
    cnt = int(redis_client.get(cnt_key))
    keys = sorted(redis_client.keys('doctor:*'))

    if not cnt:
        cnt = db.doctors.find().count()

    cnt = int(cnt)

    doctor_id = db.doctors.insert_one(doctor.to_dict()).inserted_id
    doctor.id = doctor_id

    if keys:
        last_page_key = keys[-1] # last page that occur in cache
        last_page_idx = last_page_key.split(':')[1] # retrieve from key index of that page

        t = last_page_idx * page_size

        if t > cnt:
            data = redis_client.get(last_page_key)
            data = json_util.loads(data)
            data.append(doctor.to_dict())
            redis_client.set(last_page_key, json_util.dumps(data))
            redis_client.set('page_max_obj:' + str(last_page_idx),
                             str(doctor_id))

    redis_client.set(cnt_key, cnt + 1)

    return doctor_id


def insert_survey(survey):
    return db.surveys.insert_one(survey.to_dict()).inserted_id


def get_doctor_by_id(id):
    id = ObjectId(id)
    return Doctor(db.doctors.find_one({'_id' : id}))


def get_survey_by_id(id):
    id = ObjectId(id)
    return Survey(db.surveys.find_one({'_id' : id}))


def get_page_id(object_id):
    keys = sorted(redis_client.keys('page_max_obj:*'))

    for k in keys:
        if object_id <= redis_client.get(k):
            return get_id_from_key(k)

    return None


def update_doctor(id, doctor):
    id = ObjectId(id)
    s = str(id)

    page_id = get_page_id(s)
    if page_id is not None:
        page_key = 'doctor:' + str(page_id)

        data = redis_client.get(page_key)
        data = json_util.loads(data)

        for i in range(len(data)):
            if str(data[i]['_id']) == s:
                d = doctor.to_dict()
                d['_id'] = s
                data[i] = d
                redis_client.set(page_key, json_util.dumps(data))
                break

    return db.doctors.update_one({'_id' : id}, {"$set": doctor.to_dict()})


def get_id_from_key(key):
    return int(key.split(':')[1])


def delete_doctor(id):
    cnt = redis_client.get(cnt_key)
    if cnt:
        redis_client.set(cnt_key, int(cnt) - 1)

    keys = sorted(redis_client.keys('doctor:*'))

    page_id = get_page_id(str(id))
    page_key = 'doctor:' + str(page_id)

    gte_keys = list(filter(lambda x: x >= page_key, keys))

    next_page = json_util.loads(redis_client.get(page_key))

    next_page = list(filter(lambda x: str(x['_id']) != str(id), next_page))

    for i in range(len(gte_keys)):
        if i == (len(gte_keys) - 1) or \
                                get_id_from_key(gte_keys[i]) + 1 != get_id_from_key(gte_keys[i + 1]):
            redis_client.delete(gte_keys[i])
            break

        curr = next_page
        next_page = json_util.loads(redis_client.get(gte_keys[i + 1]))
        curr.append(next_page[0])

        page_max_key = "page_max_obj:" + str(get_id_from_key(gte_keys[i]))
        redis_client.set(page_max_key, next_page[0])

        del next_page[0]

        redis_client.set(gte_keys[i], json_util.dumps(curr))

    id = ObjectId(id)
    for survey in db.surveys.find({'doctor_ref.$id': id}):
        delete_survey(Survey(survey).id)
    return db.doctors.delete_one({'_id' : id})


def update_survey(id, survey):
    id = ObjectId(id)
    return db.surveys.update_one({'_id' : id}, {"$set": survey.to_dict()})


def delete_survey(id):
    id = ObjectId(id)
    return db.surveys.delete_one({'_id' : id})


def get_doctors_choices():
    return tuple([tuple([x['_id'], x['name'] + ' ' + x['surname']]) for x in db.doctors.find()])


def get_symptoms_choices():
    choices = ["heat", "pain", "insomnia", "inattention", "impotence", "allergy", "anemia", "blood"]
    choices += ["tumor", "diarrhea", "double vision", "weakness", "vertigo", "tremor", "sneezing"]
    choices += ["snoring", "paranoia", "osteopenia", "hyperactivity", "cough"]
    return tuple([tuple([x, x]) for x in choices])


def find_surveys(search):
    return [Survey(x) for x in db.surveys.find({'$text': {'$search': search}})]


def get_position_cnt():
    mapper = Code(
        """
        function(){
          emit(this.position, 1);
        }
        """)
    reducer = Code(
        """
          function(key, values){
            return values.length;
          };
        """)
    result = db.doctors.map_reduce(mapper, reducer, "position_res")

    lst = list(result.find().sort('value', pymongo.DESCENDING))
    for x in lst:
        x['name'] = x['_id']
        x['value'] = int(x['value'])
    return lst


def get_disease_stats():
    pipeline = [{"$unwind": "$diagnosis"},
                {"$group": {"_id": "$diagnosis", "count": {"$sum": 1}}},
                {"$sort": SON([("count", -1), ("_id", -1)])}]
    lst = list(db.surveys.aggregate(pipeline))
    for x in lst:
        x['name'] = x['_id']
    return lst


def get_hospital_personal_cnt():
    mapper = Code(
        """
        function(){
          emit(this.hospital.name, 1);
        }
        """)
    reducer = Code(
        """
          function(key, values){
            return values.length;
          };
        """)
    result = db.doctors.map_reduce(mapper, reducer, "myresults")

    lst = list(result.find().sort('value', pymongo.DESCENDING))
    for x in lst:
        x['name'] = x['_id']
        x['value'] = int(x['value'])
    return lst


def clear_cache():
    redis_client.flushdb()
