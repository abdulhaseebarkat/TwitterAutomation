import tweepy
import logging
import time
logging.basicConfig(level=logging.INFO)

# Twitter API credentials
TWITTER_CONSUMER_KEY = "yQT7K22Xpdk5foo5AYvg0NBmW"
TWITTER_CONSUMER_SECRET_KEY = "6ZWdtcOfdQYwEt4XriDf5O8TzbeTJOUMFE3KyzlWdqhs9U3ObN"
TWITTER_ACCESS_TOKEN = "1497293196413607937-p5meIP8Lc2OubkFqc4ewVXpN0Pe2eM"
TWITTER_ACCESS_TOKEN_SECRET = "ZUgq0G4rJHEh19Z2VDSrraXi2x58QXCD83ofmODOltmUv"
BEARER_TOKEN = r"AAAAAAAAAAAAAAAAAAAAACqivQEAAAAAMEAOJGAV1XTmGyILPfcy45y6XfQ%3D7GmA0e4YSDZYaFJYCn4cM4OnnF9F0WiFyloRP1RzOOYB0U0NR1"

# Initialize the Client
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=TWITTER_CONSUMER_KEY,
    consumer_secret=TWITTER_CONSUMER_SECRET_KEY,
    access_token=TWITTER_ACCESS_TOKEN,
    access_token_secret=TWITTER_ACCESS_TOKEN_SECRET
)

# Specifying accounts to monitor
accounts_to_monitor = ["haseeb_barkat"]


# Function to check and respond to tweets
def check_and_respond():
    try:
        for account in accounts_to_monitor:
            logging.info(f'Checking Tweets from {account}')
            # Fetch the latest tweets from the user timeline
            user_id = client.get_user(username=account).data.id
            tweets = client.get_users_tweets(id=user_id, tweet_fields=['id', 'text'])

            if tweets.data:
                for tweet in tweets.data:
                    tweet_id = tweet.id
                    tweet_text = tweet.text
                    logging.info(f'Responding to tweet: {tweet_text}')
                    response_text = "This is an automated response!"

                    # Reply to the tweet
                    client.create_tweet(in_reply_to_tweet_id=tweet_id, text=response_text)
                    logging.info("Response sent successfully!")
    except Exception as e:
        logging.error(f"ERROR occurred: {e}")


while True:
    check_and_respond()
    time.sleep(10)