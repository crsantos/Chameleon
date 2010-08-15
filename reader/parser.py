import feedparser
d = feedparser.parse("http://9gag.com/rss/site/feed.rss")
#d = feedparser.parse("http://feeds.feedburner.com/ffffound/everyone")

print d['feed']['title']

print "\nENTRIES:\n"
for entry in d['entries']:
    print 40*"-"
    print "title: "+str(entry['title'])
    print "links: "+str(entry['links'][0]['href'])
    print "content: "+str(entry['content'][0]['value'])

print "\n"+50*"*"

# print "\nTests\n"
# print [entry['content'] for entry in d['entries']]
