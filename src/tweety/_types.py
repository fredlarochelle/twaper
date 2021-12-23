import csv
from .utils import WORKBOOK_HEADERS


class TweetDict:
    def __init__(self, dictionary):
        self.dict_ = dictionary

    def to_csv(self,filename=None):
        all_tweets = self.dict_['tweets']
        if not filename:
            filename = "tweets.csv"
        with open(filename,"w",encoding="ASCII",errors="ignore",newline="") as csv_:
            writer = csv.writer(csv_)
            writer.writerow(WORKBOOK_HEADERS)
            for i in all_tweets:
                for p in i['result']['tweets']:
                    created_on = p['created_on']
                    is_retweet = p['is_retweet']
                    is_reply = p['is_reply']
                    tweet_id = p['tweet_id']
                    tweet_body = p['tweet_body']
                    language = p['language']
                    likes = p['likes']
                    retweet_count = p['retweet_counts']
                    source = p['source']
                    symbols = p['symbols']
                    media_ = ""
                    if not isinstance(p['media'], str):
                        for media in p['media']:
                            media_ = f"{media_} {media['expanded_url']};"
                    else:
                        media_ = p['media']
                    user_mentions = ""
                    if not isinstance(p['user_mentions'], str):
                        for user in p['user_mentions']:
                            user_mentions = f"{user_mentions} {user['screen_name']};"
                    else:
                        user_mentions = p['user_mentions']
                    hashtags = ""
                    if not isinstance(p['hashtags'], str):
                        for tag in p['hashtags']:
                            hashtags = f"{hashtags} {tag['text']};"
                    else:
                        hashtags = p['hashtags']
                    urls = ""
                    if not isinstance(p['urls'], str):
                        for url in p['urls']:
                            urls = f"{urls} {url['expanded_url']};"
                    else:
                        urls = p['urls']
                    row = [created_on,is_retweet,is_reply,tweet_id,tweet_body,language,likes,retweet_count,source,media_,user_mentions,urls,hashtags,symbols]
                    writer.writerow(row)

    def to_dict(self):
        return self.dict_
