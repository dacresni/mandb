# a file to parse the code of the man pages 
import re
from os import listdir
from django.db import models 
from models import Manual, Function
# the following strings are to regular expressions to find 

# I do believe that there are a few manuals with more than one header
def scan(file):
    man = Manual.create()
    funct_list = []
    #header_list = []
    for line in file:
        if line.beginswith(".Dd")
           man.date=line
        if line.beginswith(".Dt") #note this is the manual's name, see brk sbrk
           man.name=line
        if line.beginswith(".Nd")
           man.whatis=line
        if line.beginswith(".Fo")
           funct_list.append(line)
        if line.beginswith(".Fd")
           #header_list.append(line.split()[2])
           man.header = line.split().[2]
    mankey = man.save()
    for f in funct_list:
        funct = Function(name=f,manual=man).save()
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
    for page in listdir("./static/manzip")
        manname = page.split(".")[0]
        man = open(manname, 'r')
        scan(man)
        man.close()

if __name__ == '__main__' :
    get_pages()
