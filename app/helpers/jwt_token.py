import jwt
from helpers.ijwt_token import IJwttokenHelperClass
from helpers.logger import StreamLogger

class JwtTokenHelperClass(IJwttokenHelperClass):
    def __init__(self):
        self.stream_logger = StreamLogger.getLogger(__name__)

    def generate_jwt_token(self,content):
        encoded_content = jwt.encode(content, "316164C75800E7839D54CFC09B224513E729AC9A350C7CC11427A037928352ED", algorithm="HS256")
        token = str(encoded_content).split("'")[1]
        return token