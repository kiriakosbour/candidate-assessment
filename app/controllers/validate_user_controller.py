from helpers.logger import StreamLogger
from services.ivalidate_user import IValidateUserService
class ValidateUserController():
    def __init__(self,service:IValidateUserService):
        self.stream_logger = StreamLogger.getLogger(__name__)
        self.service = service
    def validate_user_controller(self,email,password):
        self.stream_logger.info("Validating User...")
        token = self.service.authenticate(email,password)
        return {"jwt_token":token}