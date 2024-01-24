A simple script to display the latest post from the r/PhotoshopRequest subreddit.

To use this script, you need to create a Reddit app:

    1. Visit https://www.reddit.com/prefs/apps.
    2. Under 'developer applications', click 'create another app'.
    3. Follow the setup process.
    4. Create a .env file with the following format:
            CLIENT_ID=<locate this under the name of your app where it says "personal use script">
            CLIENT_SECRET=<this is labeled as 'secret'>
            USER_AGENT=script:subreddit_notifier:v1.0 (by /u/yourusername)
    5. Enjoy.
