# -*- coding: utf-8 -*-
import sys
from HTMLParser import HTMLParser
import urllib, urllib2, cookielib
import os, time
import xml.dom.minidom

from datetime import *  
#import locale
from decimal import Decimal
from re import sub

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def download(folder, key, volume):
    baseUrl = "http://dsr.nii.ac.jp/toyobunko/"
    baseUrl += key + "/V-"
    baseUrl += str(volume) + "/images/gray/"
    for i in range(1, 1000):
        page = ("%04d" % (i)) + ".jpg"
        url = baseUrl + page
        print url
        try:
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)  
            downloaded = response.read()
            f = open(folder+"/"+"V-"+str(volume)+"/"+page, "wb")
            f.write(downloaded)
            f.close()
        except Exception, e:
            print e
            
    
download("HistoryOfTheExpeditionInAsia", "E-290.9-HE01-025", 1)
download("HistoryOfTheExpeditionInAsia", "E-290.9-HE01-025", 2)
download("HistoryOfTheExpeditionInAsia", "E-290.9-HE01-025", 3)
download("ScientificResultsOfAJourneyInCentralAsia", "E-290.9-HE01-007", 1)
download("ScientificResultsOfAJourneyInCentralAsia", "E-290.9-HE01-007", 2)
download("ScientificResultsOfAJourneyInCentralAsia", "E-290.9-HE01-007", 3)
download("ScientificResultsOfAJourneyInCentralAsia", "E-290.9-HE01-007", 4)
download("ScientificResultsOfAJourneyInCentralAsia", "E-290.9-HE01-007", 7)
download("ScientificResultsOfAJourneyInCentralAsia", "E-290.9-HE01-007", 8)
download("SouthernTibet", "VII-1-62", 1)
download("SouthernTibet", "VII-1-62", 2)
download("SouthernTibet", "VII-1-62", 3)
download("SouthernTibet", "VII-1-62", 4)
download("SouthernTibet", "VII-1-62", 5)
download("SouthernTibet", "VII-1-62", 6)
download("SouthernTibet", "VII-1-62", 7)
download("SouthernTibet", "VII-1-62", 8)
download("SouthernTibet", "VII-1-62", 9)
download("SouthernTibet", "VII-1-62", 10)
download("SouthernTibet", "VII-1-62", 11)
download("SouthernTibet", "VII-1-62", 12)

