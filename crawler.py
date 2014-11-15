import urlparse
import sys
import urllib2
from bs4 import BeautifulSoup
from datetime import datetime


if len(sys.argv) < 2:
	print "Usage = crawler.py <url>"
else:

	url=str(sys.argv[1])
	#url = "http://www.example.com"
	urls = [url]
	visited=[url]

	t1=datetime.now()
	print "crawl started at",t1

	while len(urls) < 500:
			def func():
	
					try:
						global htmltext
						htmltext = urllib2.urlopen(urls[0]).read()
					except urllib2.URLError:
						urls.pop(0)
						func()
					except KeyboardInterrupt:
						sys.exit()
					except urllib2.HTTPError, error:
						print error.read()
					if len(htmltext) == 0:
							urls.pop(0)
							func()
					else:
					
						#print urls[0]
			
						soup = BeautifulSoup(htmltext)
							
						urls.pop(0)
						if len(urls) > 2:
							urls.pop(1)
	
						for tag in soup.findAll('a',href=True):
							tag['href'] = urlparse.urljoin(url,tag['href'])
							result=urlparse.urlparse(tag['href'])
							test="http://"+result[1]
		
							if url not in test and test not in visited:
								urls.append(test)
								visited.append(test)
					
					
	
			func()
	t2=datetime.now()
	
	han=open("scanned.txt","w")
	han.write("\n".join(visited))	
	print "crawl completed in",t2-t1
