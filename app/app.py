from flask import Flask
from flask_cors import CORS
from flask import request
from flask_jwt_extended import JWTManager
from controllers.validate_user_controller import ValidateUserController
from services.validate_user import ValidateUserService
from services.connect_to_twitter import TwitterConnector
from helpers.jwt_token import JwtTokenHelperClass
from helpers.pass_hashing import PasswordHashingHelperClass
jwt = JwtTokenHelperClass()
hashing = PasswordHashingHelperClass()
twitter_connector = TwitterConnector()
validate_service = ValidateUserService(hashing,jwt)
controller =  ValidateUserController(validate_service)

def create_app():
    app = Flask(__name__)
    return app


application = create_app()


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

@application.route('/twitter', methods=['GET'])
def get_twitter():
    return twitter_connector.get_twitter("csv",50)


if __name__ == "__main__":
    application.run()
