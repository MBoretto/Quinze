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
print data


