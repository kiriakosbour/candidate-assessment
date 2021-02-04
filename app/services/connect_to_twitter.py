import twitter
from helpers.logger import StreamLogger
from helpers.config import Config
from datetime import datetime, timedelta
from wordcloud import STOPWORDS
import tweepy
import re
import json
import csv
from collections import Counter 
import operator
class TwitterConnectorService():
   
    def __init__(self):
         self.stream_logger = StreamLogger.getLogger(__name__)

    def get_twitter(self):
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
                stopwords = set(STOPWORDS)
                stopwords.add("")
                for word in list(words):
                    if word in stopwords:
                        words.remove(word)

        except Exception as exp:
            print(exp.args)
       
        return words
       

    def sort_words(self,words,format,count):
        self.stream_logger.info("Sorting word array...")
        frequency = {}
        counter = Counter()
        for word in words:
            counter[word] +=1 
        frequency = operator.itemgetter(1) #return a tuple like r[1]
        list_of_results = []
        for key, value in sorted(counter.items(), reverse=True, key=frequency):#creates atuple with key the word and value the counter and sorts them by value due to key being the r[1] element
            # results = {key:value}
            list_of_results.append(key)

        if format =="json":
            list_of_json = []
            i=0
            while i < count:
                list_of_json.append({"value":list_of_results[i]})
                i += 1
            return json.dumps(list_of_json)
        else:
            i=0     
            while i < count:
                result_file = open('filePath.csv', 'a')
                result_file.write("{}{}".format(list_of_results[i], '\n'))
                i += 1
            return {"result":"the csv is created"}
