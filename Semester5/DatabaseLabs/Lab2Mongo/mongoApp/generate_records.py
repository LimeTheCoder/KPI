import random
from pymongo.mongo_client import MongoClient

client = MongoClient()
db = client.labDb

hospital_names = ['UCLA Medical Center', 'Central Hospital', 'Johns Hopkins Hospital ', 'UPMC',
                  'Mayo Clinic', 'Brigham and Womens Hospital', 'Northwestern Memorial Hospital',
                  'Cedars-Sinai Medical Center', 'Sun Hospital', 'Moon Hospital', 'Star Hospital',
                  'Cool hospital', 'New Age Hospital', 'South Memorial Hospital', 'Red Cross Hospital']

city = ['London', 'New York', 'Boston', 'Washington', 'Preston', 'Liverpool', 'Manchester',
        'Zurich', 'Munich', 'Kyiv', 'Warsaw', 'Belgrad', 'Paris', 'Oslo', 'Bergen', 'Berlin',
        'Odesa', 'Poltava', 'Leister', 'Moskow', 'Milan', 'Rome', 'Madrid', 'Torino']

state = ['North', 'South', 'West', 'East', 'North-East', 'North-West', 'South-East', 'South-West', 'Central']

street = ['Central', 'Flowers', 'Beast', 'Hollywood', 'Stone', 'Black Eagle str', 'Saint Marsy str.']

names = ['Bob', 'Bradley', 'Jessy', 'Jesus', 'Nicholas', 'Andrew', 'Tyler', 'Logan', 'Laymont', 'Lesley',
         'Sancho', 'Maria', 'Cristina', 'Dwayne', 'Denny', 'Vladimir', 'Arsen', 'Jose', 'Zlatan', 'Joe',
         'Gabriella', 'Melissa', 'Sasha', 'Deemas', 'Wayne', 'Isabel', 'Emma', 'Olivia', 'Sophia', 'Ava', 'Emily',
         'Charlote', 'Evelyn', 'Lily', 'Scarlett', 'Hannah', 'Oliver', 'Noah', 'William', 'Jacob', 'Ethan',
         'Liam', 'Mason', 'Michael', 'Alexander', 'James', 'Benjamin', 'David', 'Matthew', 'Daniel', 'Isaac']

surnames = ['Dylan', 'Hopkins', 'Sawyer', 'Davidson', 'Cooper', 'Smith', 'Owen', 'Hunter', 'Levi', 'Rohos',
            'Terry', 'Ruiz', 'Fernandez', 'Lopez', 'Diaz', 'Gonzales', 'Johnson', 'Anderson', 'Davis',
            'Miller', 'Jones', 'Brown', 'Button', 'Thomas', 'Taylor', 'Martinez', 'Hernandez', 'Moore',
            'Wilson', 'Lee', 'Clark', 'Harris', 'Walker', 'Robinson', 'Allen', 'Yound', 'Warren',
            'Baker', 'Green', 'White', 'Adams', 'Nelson', 'Hill', 'Torres', 'Carter', 'Parker', 'Collins']

positions = ['Audiologist', 'Allergist', 'Anesthesiologist', 'Cardiologist', 'Dentist', 'Dermatologist',
             'Endocrinologist', 'Epidemiologist', 'Gynecologist', 'Immunologist', 'Microbiologist',
             'Neonatologist', 'Neurologist', 'Neurosurgeon', 'Obstetrician', 'Oncologist', 'Pediatrician',
             'Physiologist', 'Psychiatrist', 'Radiologist', 'Urologist']

def generate_hospital():
    hospital = dict()
    hospital['name'] = random.choice(hospital_names)
    hospital['city'] = random.choice(city)
    hospital['street'] = random.choice(street)
    hospital['state'] = random.choice(state)
    hospital['build_no'] = random.randrange(1, 100)
    return hospital


def generate_doctor():
    doctor = dict()
    doctor['name'] = random.choice(names)
    doctor['surname'] = random.choice(surnames)
    doctor['position'] = random.choice(positions)
    doctor['age'] = random.randrange(20, 60)
    doctor['experience'] = random.randrange(2, 22)
    doctor['hospital'] = generate_hospital()
    return doctor

for i in range(10000):
    db.doctors.insert_one(generate_doctor())