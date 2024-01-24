import os
from dotenv import load_dotenv
import praw
import time
from colorama import Fore

load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
user_agent = os.getenv('USER_AGENT')

reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)

subreddit_name = 'PhotoshopRequest'

def check_new_posts(cur_post):
    subreddit = reddit.subreddit(subreddit_name)
    for post in subreddit.new(limit=1):  
        if cur_post != post:
            cur_time = time.localtime()
            print(f"-->{Fore.RED}{cur_time.tm_mday:02d}-{cur_time.tm_mon:02d}-{cur_time.tm_year}{Fore.WHITE} | {Fore.GREEN}{cur_time.tm_hour:02d}:{cur_time.tm_min:02d}:{cur_time.tm_sec:02d}{Fore.WHITE}<--")
            print(f"\n{Fore.GREEN}New Post:{Fore.WHITE}\n____\n{post.title},\n____\n{Fore.GREEN}URL:{Fore.WHITE} {post.url}\n")
            print("_________________________________________________")
        cur_post = post
        return cur_post
            
cur_post = ""
while True:
    cur_post = check_new_posts(cur_post)
    time.sleep(10)  