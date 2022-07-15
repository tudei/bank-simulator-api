from email.policy import default
from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Api, Resource, reqparse

from routes.user import Users
from routes.user import User
from routes.transfers import Transfers


app = Flask(__name__)

CORS(app, supports_credentials=True)
api = Api(app)

class Bank_Simulator(Resource):

    def get(self):
        return "Bank Simulator Flask RestFull API"


class Bank_Simulator_Restfull_API():
    @staticmethod
    def start():
        api.add_resource(Bank_Simulator, "/bankSimulator")
        api.add_resource(Users, "/users")
        api.add_resource(User, "/user/<int:id>")
        api.add_resource(Transfers, "/transfers")
        app.run(debug=True)


if __name__ == "__main__":

    Bank_Simulator_Restfull_API.start()
