
import traceback
from utils.response import format_response
from flask import request, session, render_template
from flask_session.__init__ import Session
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from utils.db_session import provide_db_session
from api.views import blueprint

USER_INPUT = "user_input"

app = Flask(__name__)
app.config.from_object('config.Config')  # flask app configs

_session = Session(app)
_session.app.session_interface.db.create_all()

db = SQLAlchemy(app)

# register routes
app.register_blueprint(blueprint)


@app.teardown_request
def show_teardown(exception):
    if exception:
        print("teardown_request received an exception:")
        traceback.format_exc()
        # db session rollback
        db.session.rollback()
    else:
        print("Request went through without passing an exception.")

    print('app.teardown_request')


if __name__ == '__main__':
    app.run(threaded=True)
