from flask import jsonify
from flask_restful import Api, Resource, reqparse





class User(Resource):

    def get(self):
        return jsonify(users)
    