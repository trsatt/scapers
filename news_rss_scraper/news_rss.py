import feedparser
import datetime
import pymongo

def main():

    #note: atlatnic alternative feed https://www.theatlantic.com/feed/notes/
    feeds = {'abc': r'http://feeds.abcnews.com/abcnews/topstories',
             'atlantic': r'https://www.theatlantic.com/feed/all/',
             'ap': r'http://hosted2.ap.org/atom/APDEFAULT/3d281c11a96b4ad082fe88aa0db04305',
             'bbc': r'http://feeds.bbci.co.uk/news/rss.xml',
             'breitbart': r'http://feeds.feedburner.com/breitbart',
             'cnn_popular': r'http://rss.cnn.com/rss/cnn_topstories.rss',
             'cnn_us': r'http://rss.cnn.com/rss/cnn_us.rss',
             'cnn_world': r'http://rss.cnn.com/rss/cnn_world.rss',
             'cnbc': r'http://www.cnbc.com/id/100003114/device/rss/rss.html',
             'drudge_report': r'http://feeds.feedburner.com/DrudgeReportFeed',
             'democracy_now': r'https://www.democracynow.org/democracynow.rss',
             'fox_popular': r'http://feeds.foxnews.com/foxnews/most-popular',
             'fox_politics': r'http://feeds.foxnews.com/foxnews/politics',
             'fox_national': r'http://feeds.foxnews.com/foxnews/national',
             'fox_opinion' : r'http://feeds.foxnews.com/foxnews/opinion',
             'hill':r"http://thehill.com/rss/syndicator/19109",
             'hill_popular':r'http://thehill.com/rss/syndicator/19110',
             'hill_editorial':r'http://thehill.com/taxonomy/term/1114/feed',
             'hill_oped':r'http://thehill.com/taxonomy/term/1116/feed',
             'npr': r'http://www.npr.org/rss/rss.php?id=1001',
             'nyt': r'http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml',
             'nyt_world': r'http://rss.nytimes.com/services/xml/rss/nyt/World.xml',
             'nyt_national': r'http://rss.nytimes.com/services/xml/rss/nyt/US.xml',
             'nyt_politics': r'http://rss.nytimes.com/services/xml/rss/nyt/Politics.xml',
             'nyt_popular': r'http://rss.nytimes.com/services/xml/rss/nyt/MostViewed.xml',
             'nyt_editorial': r'https://www.nytimes.com/section/opinion/editorials?rss=1',
             'nyt_oped': r'https://www.nytimes.com/section/opinion/contributors?rss=1',
             'reddit_news': r'https://www.reddit.com/r/news.rss',
             'reddit_politics': r'https://www.reddit.com/r/politics.rss',
             'reddit_world': r'https://www.reddit.com/r/worldnews.rss',
             'reuters': r'http://feeds.reuters.com/reuters/topNews',
             'upi': r'http://rss.upi.com/news/top_news.rss',
             'usa_today': r'http://rssfeeds.usatoday.com/usatoday-NewsTopStories',
             'wapo_national': r'http://feeds.washingtonpost.com/rss/national',
             'wapo_politics': r'http://feeds.washingtonpost.com/rss/politics',
             'wapo_opinion': r'http://feeds.washingtonpost.com/rss/opinions',
             'wapo_world': r'http://feeds.washingtonpost.com/rss/world',
             'weekly_standard': r'http://www.weeklystandard.com/rss/all',
             'wired': r'https://www.wired.com/feed/',
             'wsj_opinion': r'http://www.wsj.com/xml/rss/3_7041.xml',
             'wsj_business': r'http://www.wsj.com/xml/rss/3_7014.xml',
             'wsj_world': r'http://www.wsj.com/xml/rss/3_7085.xml'
             }
    #news rss feeds dictoinary


    #current time
    dt = datetime.datetime.now()

    data = []
    for feed, url in feeds.items():

        rss_parsed = feedparser.parse(url)
        titles = [art['title'] for art in rss_parsed['items']]

        #create dict for each news source
        d = {
            'source':feed,
            'stories':titles,
            'datetime':dt
        }
        data.append(d)

    # Access the 'headlines' collection in the 'news' database
    client = pymongo.MongoClient()
    collection = client.news.headlines

    #insert news data
    collection.insert_many(data)

if __name__ == '__main__':
    main()
