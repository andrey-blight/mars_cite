from flask_restful import reqparse

user_parser = reqparse.RequestParser()
user_parser.add_argument('id', required=True, type=int)
user_parser.add_argument('surname', required=True)
user_parser.add_argument('name', required=True)
user_parser.add_argument('age', required=True, type=int)
user_parser.add_argument('position', required=True)
user_parser.add_argument('speciality', required=True)
user_parser.add_argument('address', required=True)
user_parser.add_argument('email', required=True)
