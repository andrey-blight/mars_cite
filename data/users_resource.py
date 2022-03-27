from flask_restful import Resource
from flask import abort, jsonify

from . import parsers
from . import db_session
from .users import User


def abort_if_users_not_found(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        abort(404, f"User {user_id} not found")


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_users_not_found(user_id)
        db_sess = db_session.create_session()
        user = db_sess.query(User).get(user_id)
        return jsonify(
            {
                'user': user.to_dict()
            }
        )

    def post(self):
        args = parsers.user_parser.parse_args()
        db_sess = db_session.create_session()
        if db_sess.query(User).get(args['id']):
            return jsonify({'error': 'Id already exists'})
        user = User(
            id=args['id'],
            city_from=args['city_from'],
            surname=args['surname'],
            name=args['name'],
            age=args['age'],
            position=args['position'],
            is_finished=args['is_finished'],
            speciality=args['speciality'],
            address=args['address'],
            email=args['email']
        )
        db_sess.add(user)
        db_sess.commit()
        return jsonify({'success': 'OK'})

    def delete(self, user_id):
        abort_if_users_not_found(user_id)
        db_sess = db_session.create_session()
        user = db_sess.query(User).get(user_id)
        db_sess.delete(user)
        db_sess.commit()
        return jsonify({'success': 'OK'})

    def put(self, user_id):
        args = parsers.user_parser.parse_args()
        db_sess = db_session.create_session()
        user = db_sess.query(User).get(user_id)
        user.id = args['id']
        user.city_from = args['city_from']
        user.surname = args['surname']
        user.name = args['name']
        user.age = args['age']
        user.position = args['position']
        user.speciality = args['speciality']
        user.address = args['address']
        user.email = args['email']
        db_sess.commit()
        return jsonify({'success': 'OK'})


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
