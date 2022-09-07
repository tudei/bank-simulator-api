from flask import jsonify
from flask_restful import Api, Resource, reqparse

from controllers.withdrawal import Withdrawal_Controller

request_put_args = reqparse.RequestParser()

request_put_args.add_argument("id_user", type=int, help="id_user is required.")
request_put_args.add_argument("amount", type=float, help="amount is required.")
request_put_args.add_argument("withdrawal_date", type=str, help="withdrawal_date is required.")

withdrawal_controller = Withdrawal_Controller()


class Withdrawals(Resource):
    def __init__(self) -> None:
        super().__init__()

    def get(self):
        return jsonify(withdrawal_controller.get_money_withdrawal())

    def post(self):
        args = request_put_args.parse_args()
        new_withdrawal = withdrawal_controller.create_new(
            id_user=args["id_user"],
            amount=args["amount"],
            withdrawal_date=args["withdrawal_date"]
        )

        return jsonify(new_withdrawal)

class Withdrawal(Resource):
    def __init__(self) -> None:
        super().__init__()

    def get(self, id):
        return jsonify(withdrawal_controller.get_money_withdrawal(id))

  

        