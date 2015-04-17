# -*- coding: utf-8 -*-
import os, time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from PIL import Image

def resizeJPG(dir):
    if (dir == ".git"):
        return
    allFiles = os.listdir(dir)
    for file in allFiles:
        if os.path.isdir(dir + "/" + file):
            print "dir: " + file
            resizeJPG(dir + "/" + file)
        elif os.path.isfile(dir + "/" + file):
            sourceNameArray = os.path.splitext(file)
            if (len(sourceNameArray) == 2) and (sourceNameArray[1] == ".jpg"): # name.jpg
                img = Image.open(dir + "/" + file)
                w,h = img.size
                m_img = img.resize((w/2, h/2), Image.BILINEAR)
                m_img.save(dir + "/" + sourceNameArray[0] + "_m" + ".jpg")
                s_img = img.resize((w/5, h/5), Image.BILINEAR)
                s_img.save(dir + "/" + sourceNameArray[0] + "_s" + ".jpg")
            print "file: " + file

resizeJPG(".")
#		if os.path.isfile(searchCondition.folder + "/src/" + imageFile) and os.path.splitext(imageFile)[1] == ".jpg" and os.path.splitext(imageFile)[0].find("A") > 0 and os.path.splitext(imageFile)[0].find("A") == (len(os.path.splitext(imageFile)[0])-1):
#			faceFiles.append([searchCondition.folder + "/src" + "/" + imageFile, searchCondition.folder + "/m_size" + "/" + os.path.splitext(imageFile)[0] + "_M" + ".jpg"]) 

