from flask import jsonify
from flask_restful import Api, Resource, reqparse

from controllers.user import User_Controller


user_controller = User_Controller()

class User(Resource):

    def get(self):

        user_controller.create_new("Nuno", "Lima", 21, "nl@gmail.com", 3000, 7197391739, "1234")
        print(user_controller.get_user())
        return jsonify({"0":"jn"})
    