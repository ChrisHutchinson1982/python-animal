from flask import Flask, render_template, request, jsonify
import os, re, datetime
import db
from models import Animal


app = Flask(__name__)

# create the database and table. Insert 10 test animals into db
# Do this only once to avoid inserting the test animals into 
# the db multiple times
if not os.path.isfile('animalsTest.db'):
    db.connect()

  

# route for landing page
# check out the template folder for the index.html file
# check out the static folder for css and js files


# @app.route("/")
# def index():
#     return 'Hello Animals'

# # def isValid(email):
# #     regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
# #     if re.fullmatch(regex, email):
# #       return True
# #     else:
# #       return False


@app.route("/request", methods=['POST'])
def postRequest():
    req_data = request.get_json()
    # email = req_data['email']
    # if not isValid(email):
    #     return jsonify({
    #         'status': '422',
    #         'res': 'failure',
    #         'error': 'Invalid email format. Please enter a valid email address'
    #     })
    name = req_data['name']
    food = req_data['food']
    animals = [a.serialize() for a in db.view()]
    for a in animals:
        if a['name'] == name:
            return jsonify({
                # 'error': '',
                'res': f'Error! Animal with animal {name} is already in library!',
                'status': '404'
            })

    animal = Animal(db.getNewId(), True, name, food, datetime.datetime.now())
    print('new animal: ', animal.serialize())
    db.insert(animal)
    new_animals = [a.serialize() for a in db.view()]
    print('animals in lib: ', new_animals)
    
    return jsonify({
                # 'error': '',
                'res': animal.serialize(),
                'status': '200',
                'msg': 'Success creating a new animal!👍😀'
            })


@app.route('/request', methods=['GET'])
def getRequest():
    content_type = request.headers.get('Content-Type')
    animals = [a.serialize() for a in db.view()]
    if (content_type == 'application/json'):
        json = request.json
        for a in animals:
            if a['id'] == int(json['id']):
                return jsonify({
                    # 'error': '',
                    'res': a,
                    'status': '200',
                    'msg': 'Success getting all animals in library!'
                })
        return jsonify({
            'error': f"Error! animal with id '{json['id']}' not found!",
            'res': '',
            'status': '404'
        })
    else:
        return jsonify({
                    # 'error': '',
                    'res': animals,
                    'status': '200',
                    'msg': 'Success getting all animals in library!',
                    'no_of_animals': len(animals)
                })


# @app.route('/request/<id>', methods=['GET'])
# def getRequestId(id):
#     req_args = request.view_args
#     # print('req_args: ', req_args)
#     animals = [b.serialize() for b in db.view()]
#     if req_args:
#         for b in animals:
#             if b['id'] == int(req_args['id']):
#                 return jsonify({
#                     # 'error': '',
#                     'res': b,
#                     'status': '200',
#                     'msg': 'Success getting animal by ID!👍😀'
#                 })
#         return jsonify({
#             'error': f"Error ⛔❌! animal with id '{req_args['id']}' was not found!",
#             'res': '',
#             'status': '404'
#         })
#     else:
#         return jsonify({
#                     # 'error': '',
#                     'res': animals,
#                     'status': '200',
#                     'msg': 'Success getting animal by ID!👍😀',
#                     'no_of_animals': len(animals)
#                 })

# @app.route("/request", methods=['PUT'])
# def putRequest():
#     req_data = request.get_json()
#     availability = req_data['available']
#     name = req_data['name']
#     the_id = req_data['id']
#     animals = [b.serialize() for b in db.view()]
#     for b in animals:
#         if b['id'] == the_id:
#             animal = Animal(
#                 the_id, 
#                 availability, 
#                 name, 
#                 datetime.datetime.now()
#             )
#             print('new animal: ', animal.serialize())
#             db.update(animal)
#             new_animals = [b.serialize() for b in db.view()]
#             print('animals in lib: ', new_animals)
#             return jsonify({
#                 # 'error': '',
#                 'res': animal.serialize(),
#                 'status': '200',
#                 'msg': f'Success updating the animal named {name}!👍😀'
#             })        
#     return jsonify({
#                 # 'error': '',
#                 'res': f'Error ⛔❌! Failed to update animal with name: {name}!',
#                 'status': '404'
#             })
    
    


# @app.route('/request/<id>', methods=['DELETE'])
# def deleteRequest(id):
#     req_args = request.view_args
#     print('req_args: ', req_args)
#     animals = [b.serialize() for b in db.view()]
#     if req_args:
#         for b in animals:
#             if b['id'] == int(req_args['id']):
#                 db.delete(b['id'])
#                 updated_animals = [b.serialize() for b in db.view()]
#                 print('updated_animals: ', updated_animals)
#                 return jsonify({
#                     'res': updated_animals,
#                     'status': '200',
#                     'msg': 'Success deleting animal by ID!👍😀',
#                     'no_of_animals': len(updated_animals)
#                 })
#     else:
#         return jsonify({
#             'error': f"Error ⛔❌! No animal ID sent!",
#             'res': '',
#             'status': '404'
#         })

if __name__ == '__main__':
    app.run()