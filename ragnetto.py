#!/usr/bin/python

import httplib
import HTMLParser
from urlparse import urlsplit, urlparse, parse_qs

######################################################################
# Classe che trova i link ad altre stazioni
#
# inspired by: http://docs.python.org/2/library/htmlparser.html
# http://stackoverflow.com/questions/3276040/how-can-i-use-the-python-
# htmlparser-library-to-extract-data-from-a-specific-div
######################################################################
#
# create a subclass and override the handler methods

class Id_stazioni(HTMLParser.HTMLParser):
	def __init__(self):
		HTMLParser.HTMLParser.__init__(self)
		self.F_a = 0
		self.Id = 0			
		self.stazioni = dict()

	def handle_starttag(self, tag, attrs):
		if tag == 'a':			
			#print attrs
			#print len(attrs)
			for i in range(len(attrs)):
				if attrs[i][0] == 'href':
					linkStruct = urlsplit(attrs[i][1])
					if linkStruct.path == 'QO_Arrivi_SiPMR.aspx':
						self.F_a = 1						
						explode_query = parse_qs(
							urlparse(attrs[i][1]).query)
						self.Id = explode_query['Id'][0]
						#print self.Id						


	def handle_endtag(self, tag):
		if tag == 'a':
			self.F_a = 0

	def handle_data(self, data):
		if self.F_a == 1:			
			data = data.strip(' \t\n\r')
			#############################################################
			# bisogna inserire un controllo che mi filtra i link con i 
			# numeri e i caratteri delle pagine.
			#############################################################
			self.stazioni[str(self.Id)] = data			
			#print self.stazioni[str(self.Id)]
						

	def get_result(self):
        	return self.stazioni


######################################################################


stazioni= dict()
stazioni['2672']= 'Torino+Porta+Nuova'



i = 0
while i < 30 :

	chiavi_stazioni = stazioni.keys()

	conn = httplib.HTTPSConnection('prm.rfi.it',443)
	#scommentare per debug
	#conn.set_debuglevel(1)
	print 'interazione' , i
	conn.request('GET','/qo_prm/QO_Arrivi_SiPMR.aspx'
		+ '?'
		+ 'car1=' + 'arrivi'
		+ '&dalle=' + '04.00'
		+ '&alle=' + '08.00'
		+ '&txtStazione=' + stazioni[chiavi_stazioni[i]]
		+ '&x=' + '39'
		+ '&y=' + '11'
		+ '&Id=' + chiavi_stazioni[i]
		+ '&pag=' + '01'
		+ '&start=' + '0'
		+ '&stop=' + '6'
		+ '&partenzeAddrVal='  
		+ 'http%3A%2F%2Fprm.rfi.it%2Fqo_prm%2FQO_Partenze_SiPMR.aspx')

	response = conn.getresponse()

	if response.status == 200 :
		data = response.read()
		conn.close()
		#print data

		# instantiate the parser and fed it some HTML
		parser = Id_stazioni()
		parser.feed(data)
		stazioni_nuove = parser.get_result()
		#del stazioni_nuove[chiavi_stazioni[0]]
		#print stazioni_nuove
		#chiavi_stazioni = stazioni.keys()
		#print chiavi_stazioni
		stazioni.update(stazioni_nuove)
		print stazioni
		print

	else:
		print 'Errore: ', response.status, response.reason
		#print  chiavi_stazioni[i] , stazioni[chiavi_stazioni[i]]

	i = i + 1
		
