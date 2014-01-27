#!/usr/bin/python

import httplib

conn = httplib.HTTPSConnection('prm.rfi.it',443)
#scommentare per debug
#conn.set_debuglevel(1)

conn.request('GET','/qo_prm/QO_Arrivi_SiPMR.aspx'
	+ '?'
	+ 'car1=' + 'arrivi'
	+ '&dalle=' + '04.00'
	+ '&alle=' + '08.00'
	+ '&txtStazione=' + 'Torino+Porta+Nuova'
	+ '&x=' + '39'
	+ '&y=' + '11'
	+ '&Id=' + '2672'
	+ '&pag=' + '01'
	+ '&start=' + '0'

	+ '&stop=' + '6'
	+ '&partenzeAddrVal=' + 
	'http%3A%2F%2Fprm.rfi.it%2Fqo_prm%2FQO_Partenze_SiPMR.aspx'

	)

response = conn.getresponse()
print response.status, response.reason

data = response.read()
conn.close()
#print data

#preso da http://docs.python.org/2/library/htmlparser.html
# http://stackoverflow.com/questions/3276040/how-can-i-use-the-python-htmlparser-library-to-extract-data-from-a-specific-div


import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser.HTMLParser):
	def __init__(self):
		HTMLParser.HTMLParser.__init__(self)
		self.F_tr = 0
		self.F_td = 0
		self.data = []

	def handle_starttag(self, tag, attrs):
		if tag == 'tr':
			self.F_tr = 1
		if tag == 'td':
			self.F_td = 1

	def handle_endtag(self, tag):
		if tag == 'tr':
			self.F_tr = 0
		if tag == 'td':
			self.F_td = 1

	def handle_data(self, data):
		if self.F_tr == 1 and self.F_td == 1:
			data = data.strip(' \t\n\r')
			print data 

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed(data)
