from flask_restful import Resource,abort
from models import Answer, Question, with_row_locks
from utils.db_session import provide_db_session
from flask import request
from datetime import datetime
class OneAnswerResource(Resource):

    def get(self,qn_id,ans_id): # get an answer
        Answer.get(ans_id)
        #TODO:

    @provide_db_session
    def put(self, qn_id, ans_id, db=None):  # update an answer
        json_data = request.get_json(force=True)
        new_content = json_data.get('content',None)
        new_likes = json_data.get('likes',None)
        new_dislikes = json_data.get('dislikes',None)

        existing_answer = Answer.get(ans_id)

        if not existing_answer:
            abort(404)

        if new_content:
            existing_answer.content = new_content
        if new_likes:
            existing_answer.likes = new_likes
        if new_dislikes:
            existing_answer.dislikes = new_dislikes

        db.session.add(existing_answer)

        return {"msg": "Updated answer={}".format(ans_id)}, 200

    def delete(self,qn_id, ans_id): # delete an answer
        Answer.delete(ans_id)

        return {"msg": "Delete answer={}".format(ans_id)}, 200


class OneQuestionAnswersResource(Resource):
    @provide_db_session
    def get(self,qn_id,db=None): # get all answers of a question
        ans_list = with_row_locks(db.session.query(Answer).filter(Answer.qn_id == qn_id).order_by(Answer.created_at)).all()
        #TODO:

    @provide_db_session
    def post(self,qn_id,db=None): # add new answer to a question
        json_data = request.get_json(force=True)

        content = json_data.get('content', None)
        if not content:
            abort(400)

        new_answer = Answer(qn_id, content)

        db.session.add(new_answer)

        return {"msg": "Added answer={} to qn={}".format(content,qn_id)}, 200

    @provide_db_session
    def delete(self,qn_id,db=None): # delete all answers of a question
        with_row_locks(db.session.query(Answer).filter(
            Answer.qn_id == qn_id)).delete()

        return {"msg": "Deleted all answers of qn={}".format( qn_id)}, 200
