import feedparser
d = feedparser.parse("http://9gag.com/rss/site/feed.rss")
print d['feed']['title']