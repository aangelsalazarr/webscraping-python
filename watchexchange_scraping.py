# this is the API that allows us to grab data from subreddits
import praw

# information from creating an app
my_client_id = 'oNiqOTx0INdAvxJ-kEs2Qg'
my_client_secret = 'b8bgr02-xALNovaZqSgGFAP2eoZTPQ'
my_user_agent = 'webscraping'

# purpose is to authenticate ourselves
reddit = praw.Reddit(client_id=my_client_id, client_secret=my_client_secret, user_agent=my_user_agent)

