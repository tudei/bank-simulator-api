from flask import jsonify
from flask_restful import Api, Resource, reqparse

from controllers.transfers import Transfers_Controller

request_put_args = reqparse.RequestParser()

request_put_args.add_argument("id_sender", type=int, help="id_sender is required.")
request_put_args.add_argument("id_receiver", type=int, help="id_receiver is required.")
request_put_args.add_argument("amount", type=float, help="amount is required.")
request_put_args.add_argument("transfer_date", type=str, help="transfer_date is required.")

transfer_controller = Transfers_Controller()
class Transfers(Resource):

    def get(self):
        return jsonify(transfer_controller.get_transfers())

    def post(self):
        args = request_put_args.parse_args()

        new_transfer = transfer_controller.create_new(
            id_sender=args["id_sender"],
            id_receiver=args["id_receiver"],
            amount=args["amount"],
            transfer_date=args["transfer_date"],
        )


        return jsonify(new_transfer)