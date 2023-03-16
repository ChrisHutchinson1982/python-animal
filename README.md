# Python CRUD app with Flask

## This is an extremely small API using Python3, Flask and a SQLite database.

In your terminal, run the following code to install dependencies:

```
>>> pip install flask
```

In your terminal, run the following code to start your Flask server:

```
> > > flask run
```

test the api using Postman, open the database with DBeaver to see the cars table and its data.

HTTP GET request => http://127.0.0.1:5000

```json
{
  "success": true,
  "message": "our API works"
}
```

HTTP GET request => http://127.0.0.1:5000/request

```json
{
  "msg": "Success getting all animals in library!",
  "no_of_animals": 6,
  "res": [
    {
      "available": true,
      "food": "Insects, spiders, fruits, and seeds",
      "id": 5220804,
      "name": "Blue Tit",
      "timestamp": "2023-03-16 13:50:35.720707"
    },
    {
      "available": true,
      "food": "Insects, spiders, worms, and seeds",
      "id": 30092845,
      "name": "House Sparrow",
      "timestamp": "2023-03-16 13:50:35.720709"
    },
    {
      "available": true,
      "food": "Rabbits, mice, voles, birds, frogs, fish, eggs, and fruits and vegetables",
      "id": 80614251,
      "name": "Red Fox",
      "timestamp": "2023-03-16 13:50:35.720708"
    },
    {
      "available": true,
      "food": "Insects, spiders and worms",
      "id": 93921864,
      "name": "European Robin",
      "timestamp": "2023-03-16 13:50:35.720703"
    },
    {
      "available": true,
      "food": "Insects, fruit, carrion",
      "id": 189012277,
      "name": "Crow",
      "timestamp": "2023-03-16 13:50:35.720708"
    },
    {
      "available": true,
      "food": "Worms, Roots, Fruit",
      "id": 248290998,
      "name": "Badger",
      "timestamp": "2023-03-16 13:50:35.720708"
    }
  ],
  "status": "200"
}
```
