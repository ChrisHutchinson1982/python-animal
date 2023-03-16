import sqlite3, random, datetime
from models import Animal


def getNewId():
    return random.getrandbits(28)

animals = [
    # {
    #     'available': True,
    #     'name': 'European Robin',
    #     'food': 'Insects, spiders and worms',
    #     'timestamp': datetime.datetime.now()
    # },
    {
        'available': True,
        'name': 'European Robin',
        'food': 'Insects, spiders and worms',
        'timestamp': datetime.datetime.now()
    },
    {
        'available': True,
        'name': 'Blue Tit',
        'food': 'Insects, spiders, fruits, and seeds',
        'timestamp': datetime.datetime.now()
    },
    {
        'available': True,
        'name': 'Red Fox',
        'food': 'Rabbits, mice, voles, birds, frogs, fish, eggs, and fruits and vegetables',
        'timestamp': datetime.datetime.now()
    },
    {
        'available': True,
        'name': 'Badger',
        'food': 'Worms, Roots, Fruit',
        'timestamp': datetime.datetime.now()
    },
    {
        'available': True,
        'name': 'Crow',
        'food': 'Insects, fruit, carrion',
        'timestamp': datetime.datetime.now()
    },
    {
        'available': True,
        'name': 'House Sparrow',
        'food': 'Insects, spiders, worms, and seeds',
        'timestamp': datetime.datetime.now()
    },
]    

def connect():
    conn = sqlite3.connect('animalsTest.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS animals (id INTEGER PRIMARY KEY, available BOOLEAN, name TEXT, food TEXT, timestamp TEXT)")
    conn.commit()
    conn.close()
    for i in animals:
        animal = Animal(getNewId(), i['available'], i['name'],  i['food'], i['timestamp'])
        insert(animal)

def insert(animal):
    conn = sqlite3.connect('animalsTest.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO animals VALUES (?,?,?,?,?)", (
        animal.id,
        animal.available,
        animal.name,
        animal.food,
        animal.timestamp
    ))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('animalsTest.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM animals")
    rows = cur.fetchall()
    animals = []
    for i in rows:
        animal = Animal(i[0], True if i[1] == 1 else False, i[2], i[3], i[4])
        animals.append(animal)
    conn.close()
    return animals

def update(animal):
    conn = sqlite3.connect('animalsTest.db')
    cur = conn.cursor()
    cur.execute("UPDATE animals SET available=?, name=?, food=? WHERE id=?", (animal.available, animal.name, animal.food, animal.id))
    conn.commit()
    conn.close()

def delete(theId):
    conn = sqlite3.connect('animalsTest.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM animals WHERE id=?", (theId,))
    conn.commit()
    conn.close()

def deleteAll():
    conn = sqlite3.connect('animalsTest.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM animals")
    conn.commit()
    conn.close()