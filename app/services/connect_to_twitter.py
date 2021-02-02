import twitter
from helpers.logger import StreamLogger
from helpers.config import Config
from datetime import datetime, timedelta
import tweepy
import re
import json
import csv

class TwitterConnector():
   
    def __init__(self):
         self.stream_logger = StreamLogger.getLogger(__name__)
    
    def get_twitter(self,format,count):
        self.stream_logger.info("Connecting to twitter..")
        consumer_key = Config.getParam("twitter_api","api_key")
        consumer_secret = Config.getParam("twitter_api","api_secret_key")
        api_token = Config.getParam("twitter_api","access_token")
        api_token_secret = Config.getParam("twitter_api","access_token_secret")
        auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
        auth.set_access_token(api_token,api_token_secret)
        twitter_api = tweepy.API(auth)
        last_24hour_date_time = datetime.now() - timedelta(hours = 24)
        end_date = datetime.now().strftime("%Y-%m-%d")
        startDate = last_24hour_date_time.strftime("%Y-%m-%d")
        text = ""
        words = []
        try:
            tweets = tweepy.Cursor(twitter_api.search,q="#Marvel",lang="en",remove = [],since=startDate,until=end_date).items(100)
            for tweet in tweets:
                text += tweet.text.lower()
                no_links = re.sub(r'http\S+', '', text)
                no_unicode = re.sub(r"\\[a-z][a-z]?[0-9]+", '', no_links)
                no_special_characters = re.sub('[^A-Za-z ]+', '', no_unicode)
                words = no_special_characters.split(" ")
                words = [w for w in words if len(w) > 3]  # ignore a, an, be, for,and ...
        except Exception as exp:
            print(exp.args)
        list_of_json = []
        if format =="json":
            i=0
            while i < count:
                list_of_json.append(words[i])
                i += 1
            return json.dumps(list_of_json)
        else:
            i=0     
            while i < count:
                result_file = open('filePath.csv', 'a')
                result_file.write("{}{}".format(words[i], '\n'))
                i += 1
            return {"result":"the csv is created"}

