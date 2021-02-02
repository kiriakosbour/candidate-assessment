from helpers.logger import StreamLogger
from services.ivalidate_user import IValidateUserService
from helpers.ipass_hashing import IPasswordHashingHelperClass
from entities.user import User
from helpers.ijwt_token import IJwttokenHelperClass

class ValidateUserService(IValidateUserService):
    def __init__(self,hash:IPasswordHashingHelperClass,jwt:IJwttokenHelperClass):
        self.stream_logger = StreamLogger.getLogger(__name__)
        self.hash = hash
        self.jwt = jwt

    def validate_user_credentials(self,email,password):
       
        current_user = User(email=email,password=password)
        password_hash = self.hash.generate_hash(password)
        saved_password_hash = open("pass.txt", "r")
        if password_hash == saved_password_hash.read():
            user_email = current_user.email
            jwt_token = self.jwt.generate_jwt_token({"email": user_email})
            return jwt_token
        else:
            return self.stream_logger.info("Error generating jwt")
