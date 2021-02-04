from helpers.logger import StreamLogger
from services.iconnect_to_twitter import ITwitterConnectorService
class TwitterConnectionController():
    def __init__(self,service:ITwitterConnectorService):
        self.stream_logger = StreamLogger.getLogger(__name__)
        self.service = service

    def get_twitter_word_cloud_controller(self,format,word_count):
        self.stream_logger.info("Creating World Cloud...")
        if format != 'json' and format != 'csv':
            print(format)
            return {"Message": f"Bad request the format must be json or csv ."}, 400
        words = self.service.get_twitter()
        response = self.service.sort_words(words,format,word_count)
        return response