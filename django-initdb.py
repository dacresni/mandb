#! /usr/bin/env python
# a file to parse the code of the man pages 
import re
import os
from datetime import datetime
os.environ['DJANGO_SETTINGS_MODULE'] = 'mandb.settings'
from django.conf import settings
from mandb import models 

# the following strings are to regular expressions to find 

# I do believe that there are a few manuals with more than one header
def scan(file):
    man = models.Manual()
    funct_list = []
    newheader = models.Header()
    for line in file:
        if line.startswith(".Dd"):
            timeString = " ".join(line.strip(",\n").split()[1:])
            man.date=datetime.strptime(timeString,"%B %d, %Y")
        if line.startswith(".Dt"): #note this is the manual's name, see brk sbrk
           man.name=line
        if line.startswith(".Nd"):
           man.whatis=line
        if line.startswith(".Fo"):
           funct_list.append(line)
        if line.startswith(".Fd"):
           #man.header =line.split()[2]
           newheader = models.Header(name = line.split()[2])
    #man.header = newheader.name
    man.save()
    newheader.save()
    for f in funct_list:
        funct = models.Function(name=f,manual=man).save()
#    for h in header_list :
#        head = Header.gql("WHERE name = :n" n=h)
#        head = Header.objects.filter(name = h)
    #    i head:
#            head.append(mankey)
#            head.save()
#        else:
#            head = Header(name=h)
#            head.manuals.append(k)
#            head.save()

def get_pages():
    mandir = "mandb/static/manzip"
    os.chdir(mandir)
    for page in os.listdir('.'):
        manname = page.split(".")[0]
        man = open(manname, 'r')
        scan(man)
        man.close()

if __name__ == '__main__' :
    get_pages()
