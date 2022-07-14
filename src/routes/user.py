from flask import jsonify
from flask_restful import Api, Resource, reqparse

from controllers.user import User_Controller


user_controller = User_Controller()

class User(Resource):

    def get(self):
        return jsonify(user_controller.get_user())
    