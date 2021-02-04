from helpers.logger import StreamLogger
from services.ivalidate_user import IValidateUserService
from helpers.ipass_hashing import IPasswordHashingHelperClass
from helpers.security import username_mapping

class ValidateUserService(IValidateUserService):
    def __init__(self,hash:IPasswordHashingHelperClass):
        self.stream_logger = StreamLogger.getLogger(__name__)
        self.hash = hash

    def authenticate(self,username,password):
        print(username)
        password_hash = self.hash.generate_hash(password)
        user = username_mapping.get(username,None)
        if user and user.password == password_hash:
            return user
        else:
            return self.stream_logger.info("Error authenticate user")
