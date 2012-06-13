#! /usr/bin/env python 
import re
import os 
from subprocess import Popen, PIPE, STDOUT

mandir = "/usr/share/man/man2/"
def names():
    for page in os.listdir(mandir):
        manname = page.split(".")[0]
        #command = "man 2 %s| col"%(manname) 
        command = "gzip  -cd %s"%("".join([mandir,page]))
        print command
        p = Popen(command, shell=True, stdout=PIPE, stderr=STDOUT)
        mantext= p.communicate()[0]
        #filenam = "".join([manname, ".txt" ])
        filenam = "manzip/%s"%(manname)
        print filenam 
        phage = file(filenam, 'w' )
        phage.write(mantext)
        phage.close()

   

if __name__ == '__main__' :
    names()
