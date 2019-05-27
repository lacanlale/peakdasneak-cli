from .formatter import Formatter
from datetime import datetime
from joblib import dump, load
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
import praw
import os.path

class Reddit_Scraper:
    title = Formatter()
    date = Formatter()
    comment_total = Formatter()
    pos = Formatter()
    neg = Formatter()
    title.cfg(fg='w', st='b', bg='k')
    date.cfg(fg='w', st='i')
    comment_total.cfg(fg='c', st='u')
    pos.cfg('g', st='b')
    neg.cfg('r', st='b')


    def __init__(self, client_id, client_secret, version):
        self.reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=f'cli-tool: peakdasneak:v{version} (by /u/lacanlale')
    
    # def __store(self, posts, subreddit):
    #     if not os.path.isfile('data/comments.csv'):
    #         f = open("data/comments.csv", "x")
    #         f.write('subreddit,post_id,post_title,post_comment_id,post_comment,sentiment\n')
    #         f.close()

    #     with open('data/comments.csv', 'w') as data_file:
    #         for post in posts:
    #             for comment in posts.comments:
    #                 data_file.write(f'{subreddit},{post.id},{post.title},{comment},{comment.body},')

    def scrape(self, subreddit, flair=None, limit=10, sort_by='relevance', posts_from='week'):
        """
        Scrapes specific info from stated subreddit

        Parameters
        ----------
        subreddit : str
            Desired subreddit
        flair : str
            Additional detail to search for within the subreddit. None by default
        limit : int
            Post limit to search for. 10 by default.
        sort_by : str
            Should be between 'relevance', 'top', 'new', and 'comments'. 'relevance' by default.
        posts_from : str
            Should be between 'week', 'hour', '24 hours', 'month', 'year', 'all time'. 'week' by default

        Returns
        -------
        urls : dict
            Url of corresponding post
        """
        urls = {}
        posts = []
        clf = load('model.joblib')
        ngram_vectorizer = load('ngram_vectorizer.joblib')
        
        counter = 1
        sub = self.reddit.subreddit(subreddit)
        avg = lambda l: sum(l) / len(l)
        for post in sub.search(f'flair:"{flair}"', sort=sort_by, time_filter=posts_from):
            date = datetime.fromtimestamp(post.created_utc)
            diff = datetime.utcnow() - date
            date = f"{date.month}/{date.day}/{date.year}"

            posts.append(post)
            urls[str(counter)] = post.url

            self.title.out(f"{counter}.) {post.title}", ' | ')
            self.date.out(f"Date created: {date}, {diff.days} days ago", ' | ')
            self.comment_total.out(f"Comment Total: {post.num_comments}", ' | ')

            sent = []
            for comment in post.comments:
                sent.append(clf.predict(ngram_vectorizer.transform([comment.body])))
            
            if len(sent) != 0:
                avg_sent = avg(sent)
                if avg_sent >= 0.8:
                    self.pos.out("Extremely Positive")
                elif avg_sent >= 0.6 and avg(sent) < 0.8:
                    self.pos.out("Mostly Positive")
                elif avg_sent >= 0.40 and avg_sent < 0.60:
                    print("Neutral")
                elif avg_sent < 0.40 and avg_sent >= 0.20:
                    self.neg.out("Mostly Negative")
                elif avg_sent < 0.2:
                    self.neg.out("Extremely Negative")
            else:
                print("No comments to analyze sentiment")

            counter += 1
        
        return urls
