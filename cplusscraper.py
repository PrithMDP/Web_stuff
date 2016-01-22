import urlparse
import requests
import urllib
import re
from bs4 import BeautifulSoup

url = "http://www.cplusplus.com/reference"

htmltext = (requests.get(url)).text

soup = BeautifulSoup(htmltext, 'html.parser')
header_set = set()
for link in soup.findAll('div',{'class' : 'C_doc'}):
	for url in link.findAll('a',href = True):
		#print url['href']	#put in a set
		header_set |= {url['href']}

for link in header_set:
	print link

print "\nLEVEL 2 GOING THROUGH ALL FUNCTIONS BY HEADER HERE:\n"



for link in header_set:
	baseurl = "http://www.cplusplus.com"
	baseurl += str(link)
	#print baseurl
	#baseurl = "http://www.cplusplus.com/reference/cstring/"
	htmltext = requests.get(baseurl).text

	soup = BeautifulSoup(htmltext, 'html.parser')

	for head in soup.findAll('dl',{'class' : 'links'}):
		for url in head.findAll('a', href = True):
	 			print url['href']
	print "\n"

	# add last url then open that page and use extraction to get string between last two "/"
	#that will be the key and value -> ask aaryaman what exactly to be put







	# for link in soup.findAll('section', {'id' : 'functions'}):
	# 	for row in link.findAll('dl', {'class' : 'links'}):
	# 		for url in row.findAll('a', href = True):
	# 			print url['href']