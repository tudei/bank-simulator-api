from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Api, Resource, reqparse

from src.routes.user import User


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
        api.add_resource(User, "/users")
        app.run(debug=True)


if __name__ == "__main__":

    Bank_Simulator_Restfull_API.start()
