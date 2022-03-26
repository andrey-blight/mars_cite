from flask_restful import Resource
from flask import abort

from . import parsers
from . import db_session
from .users import User


def abort_if_users_not_found(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        abort(404, message=f"User {user_id} not found")


class UsersResource(Resource):
    def get(self, user_id):
        args = parser.parse_args()
        db_sess = db_session.create_session()
        user = db_sess.query(User).get(user_id)
        if not jobs:
            return jsonify({'error': 'Not found'})
        return jsonify(
            {
                'user': user.to_dict()
            }
        )


class UsersListResource(Resource):
    def get(self):
        db_sess = db_session.create_session()
        users = db_sess.query(User).all()
        return jsonify(
            {
                'users':
                    [item.to_dict(only=('surname', 'name', 'age', 'position', 'speciality', 'address', 'email')) for
                     item in
                     users]
            }
        )
