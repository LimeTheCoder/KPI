from pymongo.database import DBRef


class Hospital(object):
    def __init__(self, attr_list={}):
        self.id = attr_list.get('_id', None)
        self.name = attr_list.get('name', '')
        self.city = attr_list.get('city', '')
        self.state = attr_list.get('state', '')
        self.street = attr_list.get('street', '')
        self.build_no = attr_list.get('build_no', -1)

    def to_dict(self):
        d = {}
        if self.name != '': d['name'] = self.name
        if self.city != '': d['city'] = self.city
        if self.state != '': d['state'] = self.state
        if self.street != '': d['street'] = self.street
        if self.build_no != -1: d['build_no'] = self.build_no
        if self.id is not None: d['_id'] = self.id

        return d

    def __str__(self):
        return self.name.encode('utf8')


class Doctor(object):
    def __init__(self, attr_list={}):
        self.id = attr_list.get('_id', None)
        self.name = attr_list.get('name', '')
        self.surname = attr_list.get('surname', '')
        self.position = attr_list.get('position', '')
        self.experience = attr_list.get('experience', -1)
        self.age = attr_list.get('age', 0)
        self.hospital = Hospital(attr_list.get('hospital', {}))

    def to_dict(self):
        d = {}
        if self.name != '': d['name'] = self.name
        if self.surname != '': d['surname'] = self.surname
        if self.position != '': d['position'] = self.position
        if self.experience != -1: d['experience'] = self.experience
        if self.age != 0: d['age'] = self.age
        if self.id is not None: d['_id'] = self.id
        h = self.hospital.to_dict()
        if h != {} : d['hospital'] = h

        return d

    def __str__(self):
        return (self.name + " " + self.surname).encode('utf8')


class Pacient(object):
    def __init__(self, attr_list={}):
        self.id = attr_list.get('_id', None)
        self.name = attr_list.get('name', '')
        self.surname = attr_list.get('surname', '')
        self.age = attr_list.get('age', 0)

    def to_dict(self):
        d = {}
        if self.name != '': d['name'] = self.name
        if self.surname != '': d['surname'] = self.surname
        if self.age != 0: d['age'] = self.age
        if self.id is not None: d['_id'] = self.id

        return d

    def __str__(self):
        return (self.name + " " + self.surname).encode('utf8')


class Survey(object):
    def __init__(self, attr_list={}):
        self.id = attr_list.get('_id', None)
        self.diagnosis = attr_list.get('diagnosis', '')
        self.is_closed = attr_list.get('is_closed', False)
        self.open_date = attr_list.get('open_date', None)
        self.pacient = Pacient(attr_list.get('pacient', {}))
        self.symptoms = attr_list.get('symptoms', [])
        ref = attr_list.get('doctor_ref', None)

        if ref is not None:
            from mongo_model import get_doctor_by_id
            self.doctor = get_doctor_by_id(ref.id)
        else:
            self.doctor = None

    def to_dict(self):
        d = {}
        if self.diagnosis != '': d['diagnosis'] = self.diagnosis
        if self.open_date is not None: d['open_date'] = self.open_date
        if self.id is not None: d['_id'] = self.id
        if self.symptoms: d['symptoms'] = self.symptoms
        p = self.pacient.to_dict()
        if p != {}: d['pacient'] = p
        d['is_closed'] = self.is_closed
        if self.doctor is not None:
            d['doctor_ref'] = DBRef('doctors', self.doctor.id)

        return d

    def pretty_symptoms(self):
        return ', '.join(self.symptoms)

    def pretty_closed(self):
        return "Closed" if self.is_closed else "Opened"

    def get_date(self):
        return self.open_date.date()

    def __str__(self):
        return (self.doctor.surname + " -> " + self.pacient.surname).encode('utf8')
