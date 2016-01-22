import urllib
import re
urls = ["http://google.com", "http://nytimes.com","http://CNN.com"]

#i = 0
#regex = '<title>.+?</title>'
#pattern = re.compile(regex)
#while i< len(urls):
#	htmlfile = urllib.urlopen(urls[i])

#	htmltext = htmlfile.read()
	
#	titles = re.findall(pattern,htmltext)
	
	#print titles
	
	#print htmltext[0:100]
#	i+=1

htmlfile = urllib.urlopen("http://finance.yahoo.com/q?s=AAPL&ql=1")

htmltext = htmlfile.read()

regex = '<span id ="yfs_l84_aapl"> (.+?) </span>'

pattern = re.compile(regex)

price = re.findall(pattern,htmltext)

print price
