#!/usr/bin/python

import httplib, csv
from urlparse import urlsplit, urlparse, parse_qs
from bs4 import BeautifulSoup
from urllib2 import urlopen

class mineCart:  
   """ Carrello da miniera per il data mining. """
   def __init__(self, seedId, seedName):
      # Saranno datamembers? Boh, io non lo conosco il Python.
      self.startingStation = str(seedId)
      self.url = str('/qo_prm/QO_Arrivi_SiPMR.aspx?'
      + 'car1=' + 'arrivi'
      + '&dalle=' + '08.00'
      + '&alle=' + '12.00'
      + '&x=' + '39'
      + '&y=' + '11'
      + '&Id=' + seedId
      + '&pag=' + '01'
      + '&start=' + '0'
      + '&stop=' + '6'
      + '&partenzeAddrVal='
      + 'http://prm.rfi.it/qo_prm/QO_Partenze_SiPMR.aspx')
      self.stations = dict()
      self.newstations = dict() 




deBug = mineCart('1234')
print deBug.startingStation
print deBug.url

