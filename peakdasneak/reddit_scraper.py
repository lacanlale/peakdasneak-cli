from .formatter import Formatter
from datetime import datetime
import praw

class Reddit_Scraper:
    title = Formatter()
    date = Formatter()
    comment_total = Formatter()
    title.cfg(fg='w', st='b', bg='k')
    date.cfg(fg='w', st='i')
    comment_total.cfg(fg='c', st='u')

    def __init__(self, client_id, client_secret, version):
        self.reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=f'cli-tool: peakdasneak:v{version} (by /u/lacanlale')
        
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
        """
        sub = self.reddit.subreddit(subreddit)
        for post in sub.search(f'flair:"{flair}"', sort=sort_by, time_filter=posts_from):
            date = datetime.fromtimestamp(post.created_utc)
            diff = datetime.utcnow() - date
            date = f"{date.month}/{date.day}/{date.year}"
            
            self.title.out(post.title, ' | ')
            self.date.out(f"Date created: {date}, {diff.days} days ago", ' | ')
            self.comment_total.out(f"Comment Total: {post.num_comments}")
