from os import path
from twitter import *
import settings


CONSUMER_KEY = settings.TWITTER_CONSUMER_KEY
CONSUMER_SECRET = settings.TWITTER_CONSUMER_SECRET

if CONSUMER_KEY is None or CONSUMER_SECRET is None:
    raise ValueError("Missing twitter credentials in settings.py file, please complete them.")

curdir = path.abspath(path.dirname(__file__))
my_twitter_creds = path.join(curdir, 'creds')

if not path.exists(my_twitter_creds):
    oauth_dance("rest vs streaming", CONSUMER_KEY, CONSUMER_SECRET, my_twitter_creds)

oauth_token, oauth_secret = read_token_file(my_twitter_creds)

auth = OAuth(oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET)

twitter_rest = Twitter(auth=auth)
twitter_stream = TwitterStream(auth=auth)
