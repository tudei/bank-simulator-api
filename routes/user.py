from flask import jsonify
from flask_restful import Api, Resource, reqparse


from controllers.user import User_Controller


add_new_args = reqparse.RequestParser()
add_new_args.add_argument("first_name", type=str, required=True, help="Frist name is required.")
add_new_args.add_argument("last_name", type=str, required=True, help="Last name is required.")
add_new_args.add_argument("age", type=int, required=True, help="Age is required.")
add_new_args.add_argument("e_mail", type=str, required=True, help="It is necessary to provide email.")
add_new_args.add_argument("balance", type=int, required=True, help="User Balance required.")
add_new_args.add_argument("nif", type=str, required=True, help="User NIF is necessary.")
add_new_args.add_argument("user_password", type=str, required=True, help="User password is necessary.")

edit_password_args = reqparse.RequestParser()
edit_password_args.add_argument("old_password", type=str, required=True, help="Old Password is required.")
edit_password_args.add_argument("new_password", type=str, required=True, help="New Password is required.")

admin_password_args = reqparse.RequestParser()
admin_password_args.add_argument("old_password", type=str, required=True, help="Old Password is required.")

user_delete_arg = reqparse.RequestParser()
user_delete_arg.add_argument("admin_password", type=str, required=True, help="Id de usuario necessario.")


user_controller = User_Controller()


class Users(Resource):

    def get(self):

        return jsonify(user_controller.get_user())

    def post(self):

        args = add_new_args.parse_args()

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

    def put(self, id):
        args = edit_password_args.parse_args()

        return jsonify(user_controller.update_user_password(id, args["new_password"]))

    def delete(self, id):

        args = user_delete_arg.parse_args()
        return jsonify(user_controller.delete_user(id, args["admin_password"]))
    