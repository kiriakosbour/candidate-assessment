from flask import Flask
from flask_cors import CORS
from flask import request
from flask_jwt import JWT, jwt_required
from controllers.validate_user_controller import ValidateUserController
from controllers.retrieve_word_cloud_controller import TwitterConnectionController 
from services.validate_user import ValidateUserService
from services.connect_to_twitter import TwitterConnectorService
from helpers.jwt_token import JwtTokenHelperClass
from helpers.pass_hashing import PasswordHashingHelperClass
from helpers.config import Config

jwt_helper = JwtTokenHelperClass()
hashing = PasswordHashingHelperClass()
twitter_service = TwitterConnectorService()
twitter_connector = TwitterConnectionController(twitter_service)
validate_service = ValidateUserService(hashing)
controller =  ValidateUserController(validate_service)

def create_app():
    app = Flask(__name__)
    return app


application = create_app()
application.secret_key = Config.getParam("jwt","application_secret_key")
jwt = JWT(application,validate_service.authenticate,jwt_helper.identity) #creates the /auth endpoint

@application.route('/health/readiness', methods=['GET'])
def readiness():
    return {'Readiness': 'Ok'}, 200
       
@application.route('/health/liveness', methods=['GET'])
def liveness():
    return {'Liveness': 'Ok'}, 200
@application.route('/login', methods=['POST'])
def login_user():
    user_email = request.json["email"]
    user_password = request.json["password"]

    user_token = controller.validate_user_controller(user_email,user_password)

    if user_token:
        return user_token
    else:
       {"error":401}

@application.route('/twitter/<int:word_count>/<format>', methods=['GET'])
@jwt_required()
def get_twitter(word_count,format):
    return twitter_connector.get_twitter_word_cloud_controller(format,word_count)


if __name__ == "__main__":
    application.run()
