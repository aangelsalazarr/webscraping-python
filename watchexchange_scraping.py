# this is the API that allows us to grab data from subreddits
import praw

# information from creating an app
my_client_id = 'oNiqOTx0INdAvxJ-kEs2Qg'
my_client_secret = 'b8bgr02-xALNovaZqSgGFAP2eoZTPQ'
my_user_agent = 'energy watch webscraping'

# purpose is to authenticate ourselves
reddit = praw.Reddit(client_id=my_client_id,
                     client_secret=my_client_secret,
                     user_agent=my_user_agent)

# we want to get hottest posts from the watch exchange subreddit
hot_posts_watch_ex = reddit.subreddit('energy').hot(limit=25)

# purpose is to print the top n posts from watch exchange
for post in hot_posts_watch_ex:
    print(post.title)

