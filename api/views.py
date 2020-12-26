from flask import Blueprint
from flask_restful import Api
from api.resources import (
  QuestionsResource,
  OneQuestionResource,
  OneQuestionAnswersResource,
  OneAnswerResource
)
blueprint = Blueprint('api', __name__, url_prefix='/api/v1')

api = Api(blueprint)

api.add_resource(QuestionsResource, '/questions')
api.add_resource(OneQuestionResource, "/questions/<int:qn_id>")

api.add_resource(OneQuestionAnswersResource, '/questions/<int:qn_id>/answers')
api.add_resource(OneAnswerResource, '/questions/<int:qn_id>/answers/<int:ans_id>')
