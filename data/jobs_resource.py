from flask_restful import Resource
from flask import abort, jsonify

from . import parsers
from . import db_session
from .jobs import Jobs
from .users_resource import abort_if_users_not_found

def abort_if_jobs_not_found(job_id):
    session = db_session.create_session()
    job = session.query(Jobs).get(job_id)
    if not job:
        abort(404, f"Job {job_id} not found")


class JobsResource(Resource):
    def get(self, job_id):
        abort_if_jobs_not_found(job_id)
        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).get(job_id)
        return jsonify(
            {
                'job': job.to_dict()
            }
        )

    def delete(self, job_id):
        abort_if_jobs_not_found(job_id)
        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).get(job_id)
        db_sess.delete(job)
        db_sess.commit()
        return jsonify({'success': 'OK'})

    def put(self, job_id):
        abort_if_jobs_not_found(job_id)
        args = parsers.job_parser.parse_args()
        db_sess = db_session.create_session()
        if job_id != args['id'] and db_sess.query(Jobs).get(args['id']):
            return jsonify({'error': 'Id already exists'})
        job = db_sess.query(Jobs).get(job_id)
        job.id = args['id']
        job.team_leader = args['team_leader']
        job.job = args['job']
        job.work_size = args['work_size']
        job.collaborators = args['collaborators']
        job.is_finished = args['is_finished']
        db_sess.commit()
        return jsonify({'success': 'OK'})


class JobsListResource(Resource):
    def get(self):
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).all()
        return jsonify(
            {
                'jobs':
                    [item.to_dict() for item in jobs]
            }
        )

    def post(self):
        args = parsers.job_parser.parse_args()
        db_sess = db_session.create_session()
        if db_sess.query(Jobs).get(args['id']):
            return jsonify({'error': 'Id already exists'})
        abort_if_users_not_found(args['team_leader'])
        job = Jobs(
            id=args['id'],
            team_leader=args['team_leader'],
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            is_finished=args['is_finished']
        )
        db_sess.add(job)
        db_sess.commit()
        return jsonify({'success': 'OK'})
