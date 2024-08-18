import tweepy
import time
import logging

logging.basicConfig(level=logging.INFO)

# Twitter API credentials
TWITTER_CONSUMER_KEY = "6QpSztvYxzdEc8VFubtZHQoA7"
TWITTER_CONSUMER_SECRET_KEY = "efiVyQWQMgNs2Flhh9PNkoQG3wiEdcFzpJpKbSCG4Mjsyl2Bie"
TWITTER_ACCESS_TOKEN = "1497293196413607937-tFeS6FpPebLUfEjRhR6L2uYKJjszXJ"
TWITTER_ACCESS_TOKEN_SECRET = "bqmEoCleN6TWCp4OZWuGBnsJsrWI4x7hzlNWhmBc95sSz"
BEARER_TOKEN = r"AAAAAAAAAAAAAAAAAAAAACqivQEAAAAAp3V%2B0SpEZdcr%2BXXuBSQNG0Lnnkc%3Dd33krczMWKfSVsj1kIH8CAnTanmZbj1aF2Aiu3HGS3A9y2YsT9"

#logging to keep track of the program in real time
logging.info("Initializing the client...")
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=TWITTER_CONSUMER_KEY,
    consumer_secret=TWITTER_CONSUMER_SECRET_KEY,
    access_token=TWITTER_ACCESS_TOKEN,
    access_token_secret=TWITTER_ACCESS_TOKEN_SECRET
)
auth = tweepy.OAuth1UserHandler(
     consumer_key = TWITTER_CONSUMER_KEY,
     consumer_secret = TWITTER_CONSUMER_SECRET_KEY,
     access_token = TWITTER_ACCESS_TOKEN,
     access_token_secret = TWITTER_ACCESS_TOKEN_SECRET
)
api = tweepy.API(auth)
logging.info("Client initialized.")
# accounts_to_monitor = ["haseeb_barkat"]

#Extracting the tweets from a text file
file_path = "tweets.txt"
with open(file_path , "r") as file:
    tweets = file.readlines()
    tweets = [tweet.strip() for tweet in tweets]

# Posting tweets automatically every 48 hours
for tweet in tweets:
    retries = 5 #retries 5 times if a tweet is not posted
    for i in range(retries):
        try:
            logging.info(f"Attempt {i+1}: Posting tweet - {tweet}")
            client.create_tweet(text = tweet)
            logging.info("Tweet successfully posted!")
            break
        except Exception as e:
            logging.error(f"Attempt {i + 1} failed: {e}")
            if i < retries - 1:
                logging.info("Waiting 10 seconds before retrying...")
                time.sleep(10)
            else:
                logging.error("Failed after multiple attempts.")
    time.sleep(48 * 3600)  # Wait 48 hours before posting the next tweet


