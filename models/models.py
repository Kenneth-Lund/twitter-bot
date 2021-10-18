from datetime import datetime

# Contains all of the twitter bot's unique parameters
class Parameters:

    def __init__(self):

        # Twitter username of author
        self.username = ""

        # Twitter password of author
        self.password = ""

        # you know where I store my chromedriver now :o
        self.chromedriver_path = r''
        # chromedriver path example: /Users/username/Downloads/chromedriver

        # Subreddit options. Bot chooses a random one from the list
        self.subreddit = []

        self.trending = []

        # Default number of retries for network requests
        self.retries = 1


# Defines the data used to post a tweet
class Tweet:

    def __init__(self, title, username, text, media_type):

        self.title = title
        self.username = username
        self.text = text
        self.media_type = media_type
        self.time_posted = datetime.now()


# Defines the user used to post a tweet
class TwitterUser:

    def __init__(self, username, login_time):

        self.username = username
        self.login_time = login_time

