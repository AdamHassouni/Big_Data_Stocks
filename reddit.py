import json
import praw
from kafka import KafkaProducer
from settings import (REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_PASSWORD,
                             REDDIT_USER_AGENT, REDDIT_USERNAME, SUBREDDITS, RAW_TOPIC, KAFKA_BOOTSTRAP_SERVERS)

reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    password=REDDIT_PASSWORD,
    user_agent=REDDIT_USER_AGENT,
    username=REDDIT_USERNAME
)

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

multi_subreddit = reddit.subreddit("+".join(SUBREDDITS))

def main():
    for submission in multi_subreddit.stream.submissions(skip_existing=True):
        data = {
            "id": submission.id,
            "title": submission.title,
            "selftext": submission.selftext,
            "created_utc": submission.created_utc,
            "subreddit": str(submission.subreddit),
            "url": submission.url,
            "author": str(submission.author) if submission.author else None
        }
        producer.send(RAW_TOPIC, data)
        producer.flush()

if __name__ == "__main__":
    main()
    
