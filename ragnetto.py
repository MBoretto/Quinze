#!/usr/bin/python

import urllib, urlparse, httplib





#params = urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})

params =  urllib.urlencode({	
	'car1':'arrivi',
	'dalle':'04.00',
	'alle':'08.00',
	'txtStazione':'Torino+Porta+Nuova',
	'x':'39',
	'y':'11',
	'Id':'2672',
	'pag':'01',
	'start':'0',

	'stop':'6',
	'partenzeAddrVal':
	'http://prm.rfi.it/qo_prm/QO_Partenze_SiPMR.aspx'

	})




headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
headers = {""}
conn = httplib.HTTPSConnection('prm.rfi.it',443)
conn.request('GET','/qo_prm/QO_Arrivi_SiPMR.aspx',params)
response = conn.getresponse()
print response.status, response.reason

data = response.read()
conn.close()
print data

print params



