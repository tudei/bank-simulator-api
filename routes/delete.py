from flask import jsonify
from flask_restful import Api, Resource, reqparse
import schemas


from controllers.user import User_Controller

class Delete(User_Controller):

    def get(self, id):

        return jsonify(user_controller.get_user(id))

    def delete_user(self, id: int, user_password: str) -> bool:
        user = self.get_user(id)
        if user["user_password"] == user_password:
            sql_query = f""" DELETE FROM user WHERE id={id}"""
            return Schema.api_response(
                status=200,
                data=self.execute_sql_query(sql_query, Schema.user),
                success_message=[Success_Message.deleted_user]
            )
        
        return Schema.api_response(
            status=503,
            error_message=[Error_Message.user_delete]
        )

    def delete(self, id):
        args = user_delete_arg.parse_args()
        return jsonify(user_controller.delete_user(id, args["user_delete"]))