from pymongo.mongo_client import MongoClient
from bson.objectid import ObjectId
from bson.son import SON
from bson.code import Code
import pymongo
import redis
from bson import json_util
from entities import Survey, Doctor
import datetime

client = MongoClient()
db = client.labDb

redis_client = redis.StrictRedis()
page_size = 50


def get_doctor_list(page):
    cnt_key = 'doctor_cnt'
    cnt = redis_client.get(cnt_key)
    if not cnt:
        cnt = db.doctors.find().count()
        redis_client.set(cnt_key, cnt)

    cnt = int(cnt)
    has_next = (cnt > (page * page_size))
    has_prev = (page > 1)


    key = 'doctor' + str(page)
    data = redis_client.get(key)

    if data:
        print 'Loaded from cache'
        return [Doctor(x) for x in json_util.loads(data)], \
               has_prev, has_next

    data = db.doctors.find().skip((page - 1) * page_size).limit(page_size)
    data = list(data)
    redis_client.set(key, json_util.dumps(data))

    print 'Loaded from database'

    return [Doctor(x) for x in data], has_prev, has_next


def get_survey_list():
    cursor = db.surveys.find()
    return [Survey(x) for x in cursor]


def insert_doctor(doctor):
    redis_client.flushdb()
    return db.doctors.insert_one(doctor.to_dict()).inserted_id


def insert_survey(survey):
    redis_client.flushdb()
    return db.surveys.insert_one(survey.to_dict()).inserted_id


def get_doctor_by_id(id):
    id = ObjectId(id)
    return Doctor(db.doctors.find_one({'_id' : id}))


def get_survey_by_id(id):
    id = ObjectId(id)
    return Survey(db.surveys.find_one({'_id' : id}))


def update_doctor(id, doctor):
    redis_client.flushdb()
    id = ObjectId(id)
    return db.doctors.update_one({'_id' : id}, {"$set": doctor.to_dict()})


def update_survey(id, survey):
    redis_client.flushdb()
    id = ObjectId(id)
    return db.surveys.update_one({'_id' : id}, {"$set": survey.to_dict()})


def delete_doctor(id):
    redis_client.flushdb()
    id = ObjectId(id)
    for survey in db.surveys.find({'doctor_ref.$id': id}):
        delete_survey(Survey(survey).id)
    return db.doctors.delete_one({'_id' : id})


def delete_survey(id):
    redis_client.flushdb()
    id = ObjectId(id)
    return db.surveys.delete_one({'_id' : id})


def get_doctors_choices():
    return tuple([tuple([x.id, str(x)]) for x in get_doctor_list()])


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


print datetime.datetime.now()