from flask_restful import Resource, abort
from models import Question, with_row_locks
from utils.db_session import provide_db_session
from flask import request, jsonify


class OneQuestionResource(Resource):
    def get(self,qn_id):
        qn = Question.get(qn_id)

        return {"msg": {"created_at": qn.created_at,
                        "content": qn.content,
                        "likes": qn.likes,
                        "dislikes": qn.dislikes}}, 200
    @provide_db_session
    def put(self,qn_id,db=None):
        json_data = request.get_json(force=True)
        new_content = json_data.get('content', None)
        new_likes = json_data.get('likes', None)
        new_dislikes = json_data.get('dislikes', None)

        existing_qn = Question.get(qn_id)

        if not existing_qn:
            abort(404)

        if new_content:
            existing_qn.content = new_content
        if new_likes:
            existing_qn.likes = new_likes
        if new_dislikes:
            existing_qn.dislikes = new_dislikes

        db.session.add(existing_qn)
        db.session.commit()

        return {"msg": "Updated question={}".format(qn_id)}, 200

    @provide_db_session
    def delete(self,qn_id,db=None):
        Question.delete(qn_id)
        db.session.commit()
        return {"msg": "Delete question={}".format(qn_id)}, 200



class QuestionsResource(Resource):

    @provide_db_session
    def get(self,db=None):
        qns_list = with_row_locks(db.session.query(Question).order_by(Question.created_at)).all()

        results = []
        for r in qns_list:
            result = {}
            result["created_at"] = r.created_at
            result["content"] = r.content
            result["likes"] = r.likes
            result["dislikes"] = r.dislikes

            results.append(result)

        return jsonify(results), 200

    @provide_db_session
    def post(self,db=None):
        json_data = request.get_json(force=True)
        content = json_data.get('content', None)

        if not content:
            abort(400)

        new_question = Question(content)

        db.session.add(new_question)
        db.session.commit()

        return {"msg": "Added new question={}".format(content)}, 200

    @provide_db_session
    def delete(self,db=None): # delete all questions
        with_row_locks(db.session.query(Question)).delete()
        db.session.commit()

        return {"msg":"deleted all questions"},200
