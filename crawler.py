import urlparse
import requests
import urllib
import re
from bs4 import BeautifulSoup

#gets all the departmental hyperlinks

url = "http://www.lsa.umich.edu/cg/cg_subjectlist.aspx?termArray=w_16_2070&cgtype=ug&allsections=true"
urls = [url]
#htmltext = urllib.urlopen(urls[0]).read()
htmltext = (requests.get(url)).text
dept_nodes=[]	#list of departments

soup = BeautifulSoup(htmltext, 'html.parser')

for link in soup.findAll('a',href=True,target='_self'):
	node = link['href']
	node = str(node)
	node +="0"	#make sure everything on 1 page
	#print node	#print the node
	dept_nodes.append(node)	
#print len(dept_nodes)
for x in range(0,334):
	url_dept = "http://www.lsa.umich.edu/cg/"
	url_dept += dept_nodes[x]
	#htmltext = urllib.urlopen(url_dept).read()
	htmltext = (requests.get(url_dept)).text
	soup = BeautifulSoup(htmltext,'html.parser')
	for link in soup.findAll('a',href=True,target='_self'):
		url_course = "http://www.lsa.umich.edu/cg/"
		link = link['href']
		url_course += link	#this is the page for each course contains the title, number etc
		#print url_course
		#htmltext = urllib.urlopen(url_course).read()
		htmltext = (requests.get(url_course)).text
		soup = BeautifulSoup(htmltext, 'html.parser')
		dept = ""
 		c_number = ""
	 	c_title = ""
	 	desc = ""
	 	for link in soup.findAll('span',{'id': 'contentMain_lblSubject'}):
 			try:
 				dept = link.contents[0]
 			except:
 				pass
 		for link in soup.findAll('span',{'id': 'contentMain_lblCatNo'}):
 			try:
 				c_number = link.contents[0]
 			except:
 				pass
 		for link in soup.findAll('span',{'id': 'contentMain_lblLongTitle'}):
 			try:
 				c_title = link.contents[0]
 			except:
 				pass
 		for link in soup.findAll('span',{'id': 'contentMain_lblDescr'}):
 			try:
 				desc = link.contents[0]
 			except:
 				pass
 		print str(dept)+" "+str(c_number)+" "+str(c_title)+" "+str(desc)+"\n"

















# url = "http://www.lsa.umich.edu/cg/cg_detail.aspx?content=2070AAPTIS364003&termArray=w_16_2070"

# urls = [url]
# visited = [url]
# while len(urls) > 0:
# 	try:
# 		htmltext = urllib.urlopen(urls[0]).read()
# 	except:
# 		pass
# 	soup = BeautifulSoup(htmltext, 'html.parser')
# 	dept = ""
# 	c_number = ""
# 	c_title = ""
# 	desc = ""
# 	try:
# 		for link in soup.findAll('span',{'id': 'contentMain_lblSubject'}):
# 			dept = link.contents[0]
# 		for link in soup.findAll('span',{'id': 'contentMain_lblCatNo'}):
# 			c_number = link.contents[0]
# 		for link in soup.findAll('span',{'id': 'contentMain_lblLongTitle'}):
# 			c_title = link.contents[0]
# 		# for link in soup.findAll('span',{'id': 'contentMain_lblDescr'}):
# 		# 	desc = link.contents[0]
# 		# 	desc.strip('<p>')	#must be a better way to do this
# 		# 	desc.srtip('</p>')
# 	except:
# 		pass
# 	print str(dept)+" "+str(c_number)+" "+str(c_title)+"\n"
# 	urls.pop(0)


# # urls = [url]	#list/queue to scrape
# # visited = [url]	#scraped or not

# # while len(urls) > 0:
# # 	try:
# # 		htmltext = urllib.urlopen(urls[0]).read()
# # 	except:
# # 		print urls[0]	#error page

# # 	soup = BeautifulSoup(htmltext, 'html.parser')


# # 	urls.pop(0) #pop first element
# # 	print len(urls)

# # 	#print (soup.get_text())
# # 	#print soup.findAll('a',href = True)
# # 	for tag in soup.findAll('a',href=True):	#has something in the anchor tag
# # 		tag['href'] = urlparse.urljoin(url,tag['href'])
# # 		if url in tag['href'] and tag['href'] not in visited:
# # 			urls.append(tag['href'])
# # 			visited.append(tag['href'])

# # print visited