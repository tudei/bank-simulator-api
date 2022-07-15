from flask import jsonify
from flask_restful import Api, Resource, reqparse


from controllers.user import User_Controller


request_put_args = reqparse.RequestParser()
request_put_args.add_argument("first_name", type=str, help="Frist name is required.")
request_put_args.add_argument("last_name", type=str, help="Last name is required.")
request_put_args.add_argument("age", type=int, help="Age is required.")
request_put_args.add_argument("e_mail", type=str, help="It is necessary to provide email.")
request_put_args.add_argument("balance", type=int, help="User Balance required.")
request_put_args.add_argument("nif", type=str, help="User NIF is necessary.")
request_put_args.add_argument("user_password", type=str, help="User password is necessary.")


user_controller = User_Controller()


class Users(Resource):

    def get(self):
        return jsonify(user_controller.get_user())

    def post(self):
        args = request_put_args.parse_args()

        new_user = user_controller.create_new(
            first_name=args["first_name"],
            last_name=args["last_name"],
            age=args["age"],
            e_mail=args["e_mail"],
            balance=args["balance"],
            nif=args["nif"],
            user_password=args["user_password"]
        )

        return jsonify(new_user)

class User(Resource):

    def get(self, id):
        return jsonify(user_controller.get_user(id))

    def put(self, id, new_password):
        new_password = new_password.lower()
        return jsonify(user_controller.update_user_password(new_password)(id))
    def delete(self, id):
        return jsonify(user_controller.delete_user(id))
    