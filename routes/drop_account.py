from flask import jsonify
from flask_restful import Api, Resource, reqparse
import resource

from controllers import Controller

request_put_args = reqparse.RequestParser()


request_put_args.add_argument("id", type=int, help="Id user is required.")
request_put_args.add_argument("amount", type=float, help="Amount is required.")
request_put_args.add_argument("drop_date", type=str, help="Drop date is required.")

sacar_controller = User_Controller()
class Sacar(Resource):

    def get(self):
        return jsonify(user_controller.get_amount())

    def post(self):
        args = request_put_args.parse_args()

    drop = user_controller.update_user_balance(
            
            id_receiver=args["id_receiver"],
            amount=args["amount"],
            drop_date=args["drop_date"],
        )


        return jsonify(new_amount)