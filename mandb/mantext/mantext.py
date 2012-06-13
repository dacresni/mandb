#! /usr/bin/env python 
import re
import os 
from subprocess import Popen, PIPE, STDOUT


def names():
    for page in os.listdir("/usr/share/man/man2/"):
        manname = page.split(".")[0]
        command = "man 2 %s| col -b"%(manname) 
        print command
        p = Popen(command, shell=True, stdout=PIPE,stderr=STDOUT )
        mantext= p.communicate()[0]
        filenam = "".join([manname, ".txt" ])
        print filenam 

        phage = file(filenam, 'w' )
        phage.write(mantext)
        phage.close()

   

if __name__ == '__main__' :
    names()
