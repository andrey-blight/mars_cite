from .db_session import SqlAlchemyBase

import datetime
import sqlalchemy
from sqlalchemy_serializer import SerializerMixin


class Departments(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'departments'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    chief = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    title = sqlalchemy.Column(sqlalchemy.String)
    members = sqlalchemy.Column(sqlalchemy.String)
    department_email = sqlalchemy.Column(sqlalchemy.String)
