# a file to parse the code of the man pages 
import re
from os import listdir
from google.appengine.ext import db
from Models import Manual, Function
 the following strings are to regular expressions to find 


def scan(file):
    man = Manual()
    funct_list = []
    header_list = []
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
           header_list.append(line.split()[2])
    mankey = man.put()
    for f in funct_list:
        funct = Function(name=f,manual=man).put()
    for h in header_list :
        head = Header.gql("WHERE name = :n" n=h)
        i head:
            head.append(mankey)
            head.put()
        else:
            head = Header(name=h)
            head.manuals.append(k)
            head.put()

def get_pages():
    for page in listdir("./static/manzip")
        manname = page.split(".")[0]
        man = open(manname, 'r')
        scan(man)
        man.close()

if __name__ == '__main__' :
    get_pages()
