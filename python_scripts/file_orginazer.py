# -*- coding: utf8 -*
import os,shutil #For os manipulation
 
cim = 0         #Initializing counts for each category
cpdf = 0
cdoc = 0
cex=0
capp =0
ctxt =0 
count = 0
ccode =0
docs = ['doc', 'docx', 'ppt', 'pptx']
images = ['jpeg', 'jpg', 'gif', 'png', 'svg', 'bat', 'bmp']
music = ['mp3', 'ogg', 'wav', 'wma']
code = ['c', 'h', 'cpp', 'cc', 'js', 'ts', 'html', 'css', 'scss', 'pyc']
os.system("mkdir images")       #Creating directories for each type
os.system("mkdir pdf")
os.system("mkdir docs")
os.system("mkdir Powerpoint")
os.system("mkdir exel")
os.system("mkdir apps")
os.system("mkdir txt")
os.system("mkdir code")
for files in os.listdir(os.getcwd()):       #Selecting images one by one     
        count=count+1
        print(files)
        if files.lower().endswith(".pdf"):
                cpdf=cpdf+1
                shutil.move(files,"pdf/")
        elif files.lower().endswith(".txt"):
                ctxt=ctxt+1
                shutil.move(files,"txt/")
        elif (files.split(".")[-1] in code):
                ccode=ccode+1
                shutil.move(files,"code/")
        elif (files.split(".")[-1] in images):
                cim=cim+1
                shutil.move(files,"images/")
        elif (files.split(".")[-1] in docs):
                cdoc=cdoc+1
                shutil.move(files,"docs/")
        elif files.lower().endswith(".exe"):
                capp=capp+1
                shutil.move(files,"apps/")
        elif (files.lower().endswith(".xlsx")) or (files.lower().endswith(".xls")):
                cex=cex+1
                shutil.move(files,"exel/")
print(count,"files detected")
print(cim,"  images moved")     #Printing counts for each type
print(cpdf,"  pdfs moved")   
print(cdoc,"  word docs moved") 
print(cex,"  exel docs moved")
print(capp,"  exe files moved")
print(ctxt,"  txt files moved")
print(ccode,"  code files moved")
s = count-(cim+cpdf+cdoc+cex+capp+ctxt+ccode)
print(s,"files left untouched")

