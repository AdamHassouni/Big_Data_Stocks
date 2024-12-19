import praw
from finbert_utiles import estimate_sentiment

reddit = praw.Reddit(
    client_id="z35mbY1mFhSd63XRWUkMZg",
    client_secret="s3a5tkRm5gpJUtNzqleUzmrzbP-4vQ",
    password="Hurlement030198-",
    user_agent="testscript by u/Sea-Consequence912",
    username="Sea-Consequence912",
)
reddits_test = []
for submission in reddit.subreddit("wallstreetbets").hot(limit=25):
    print(submission.title)
    reddits_test.append(submission.title)


probability, sentiment = estimate_sentiment(reddits_test)

