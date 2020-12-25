from flask import Blueprint
from flask_restful import Api
from api.resources import (
  QuestionListResource,
  QuestionResource,
  AnswerListResource,
  AnswerResource
)
blueprint = Blueprint('api', __name__, url_prefix='/api/v1')

api = Api(blueprint)

api.add_resource(QuestionListResource, '/questions')
api.add_resource(QuestionResource, "/questions/<int:qn_id>")

api.add_resource(AnswerListResource, '/questions/<int:qn_id>/answers')
api.add_resource(AnswerResource, '/questions/<int:qn_id>/answers/<int:ans_id>')
