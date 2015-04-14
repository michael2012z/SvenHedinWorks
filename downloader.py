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



class HtmlDownloader():

    def downLoad(self, url):
        #print "downloading file: " + url
        #request = urllib2.Request(url, self.login_data, self.headers)
        request = urllib2.Request(url)
        try:
            response = urllib2.urlopen(request)  
            downloaded = response.read()
        except Exception, e:
            print e
            downloaded = None
        return downloaded



def download(folder, pages, baseUrl):


# book History of the Expedition in Asia, 1927-1935 : vol.1
def downloadHistoryOfTheExpeditionInAsiaV1():
    folder = "HistoryOfTheExpeditionInAsiaV1"
    count = 360
    url = "http://dsr.nii.ac.jp/toyobunko/E-290.9-HE01-025/V-1/images/gray/"
    page = ("%04d" % (i)) + ".jpg"
    url += page
    print url

    request = urllib2.Request(url)
    try:
        response = urllib2.urlopen(request)  
        downloaded = response.read()
        f = open(page, "wb")
        f.write(downloaded)
        f.close()
    except Exception, e:
        print e
        downloaded = None


for i in range(1, 11):



