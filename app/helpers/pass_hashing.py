import hashlib
import os
from helpers.ipass_hashing import IPasswordHashingHelperClass
from helpers.logger import StreamLogger
class PasswordHashingHelperClass(IPasswordHashingHelperClass):
    def __init__(self):
        self.stream_logger = StreamLogger.getLogger(__name__)

    def generate_hash(self,plain_password):
        password_hash =  hashlib.sha256(b'test')
        print(password_hash)
        self.stream_logger.info("Successfullly hashed the password")
        return password_hash.hexdigest()