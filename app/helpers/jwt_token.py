import jwt
from helpers.ijwt_token import IJwttokenHelperClass
from helpers.logger import StreamLogger
from helpers.security import userid_mapping

class JwtTokenHelperClass(IJwttokenHelperClass):
    def __init__(self):
        self.stream_logger = StreamLogger.getLogger(__name__)

    def identity(self,payload):
        user_id = payload["identity"]
        return userid_mapping.get(user_id,None)