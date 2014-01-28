#!/usr/bin/python
#http://jeriwieringa.com/blog/2012/11/04/beautiful-soup-tutorial-part-1/
import httplib
from urlparse import urlsplit, urlparse, parse_qs
from bs4 import BeautifulSoup
from urllib2 import urlopen





stazioni= dict()
stazioni_nuove= dict()
stazioni['2672']= 'Torino+Porta+Nuova'



i = 0
while i < 1470 :
	stazioni_nuove= dict()
	chiavi_stazioni = stazioni.keys()

	

	conn = httplib.HTTPSConnection('prm.rfi.it',443)
	#scommentare per debug
	#conn.set_debuglevel(1)
	
	conn.request('GET','/qo_prm/QO_Arrivi_SiPMR.aspx'
		+ '?'
		+ 'car1=' + 'arrivi'
		+ '&dalle=' + '08.00'
		+ '&alle=' + '12.00'
		+ '&txtStazione=' + stazioni[chiavi_stazioni[i]]
		+ '&x=' + '39'
		+ '&y=' + '11'
		+ '&Id=' + chiavi_stazioni[i]
		+ '&pag=' + '01'
		+ '&start=' + '0'

		+ '&stop=' + '6'
		+ '&partenzeAddrVal=' + 
		'http%3A%2F%2Fprm.rfi.it%2Fqo_prm%2FQO_Partenze_SiPMR.aspx'

		)

	response = conn.getresponse()

	if response.status == 200 :
		
		data = response.read()
		conn.close()
		#print data


		soup = BeautifulSoup(data)

		#print(soup.prettify())
		#print(soup.title)
		for link in soup.find_all('a'):
			#linkStruct = urlsplit(link.get('href'))
			#if linkStruct.path == 'QO_Arrivi_SiPMR.aspx':
			indirizzo = link.get('href')
			if indirizzo != None:
				paese = link.string
			
	    			#print indirizzo , paese
				#linkStruct = urlsplit(indirizzo)
				url = urlparse(indirizzo)
				

				if url.path == 'QO_Arrivi_SiPMR.aspx':	
					paese = paese.strip(' \t\n\r')					
					paese = paese.replace(" ", "+")
					explode_query = parse_qs(url.query)
									
					#print url.query , paese
					if explode_query['Id'][0] != chiavi_stazioni[i]:
						#print explode_query['Id'][0], paese
						stazioni_nuove[str(explode_query['Id'][0])] = paese
				

		stazioni.update(stazioni_nuove)	
		

	else:
		print 'Errore: ', response.status, response.reason ,
		
	
	
	#print 'iterazione' , i
	print i , chiavi_stazioni[i] , stazioni[chiavi_stazioni[i]] , '\t\t\t\tStazioniTrovate: ' , len(stazioni) 
	#print stazioni
	#print
	


	i = i + 1
		
