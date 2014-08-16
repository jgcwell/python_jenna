"""
renames audiobook files so that they can be combined into one album
note: it did what it was supposed to do, but it was not involved in the ultimate solution
ultimate solution: select all the discs, delete disc numbers, delete files from itunes, reimport to itunes,
re-add disc numbers, rename album title to desired single title, and delete track numbers
"""

import os

## what I want the beginning to say
pretext = "HP2 Ch. "

for d,s,f in os.walk("/Users/Jenna/Desktop/HP 2"):
    for filename in f:
        if filename[0] == '.':
            continue
        if pretext in filename:
            print "skipping!"
            continue
        print filename

        ## remove leading track numbers from filenames
        filenamelist = filename.split(' ')
        if "Chapter" in filename:
            newname = ' '.join(filenamelist[2:])
        elif len(filenamelist[0]) == 2 and len(filenamelist[1]) == 3:
            newname = ' '.join(filenamelist[1:])
        else:
            newname = filename

        ## add book identifier to filename
        
        newname =  pretext + newname

        ## move out of the disc directories
        pathlist = d.split('/')
        newfolder = ' '.join(pathlist[-1].split(' ')[:-2])
##        print "newfolder: ", newfolder
        pathlist = pathlist[:-1]
        pathlist.append(newfolder)
##        print pathlist
        newpath = '/'.join(pathlist)

        newtotal = os.path.join(newpath,newname)
        print "newtotal:", newtotal
        
        ## rename file, creating new directories and removing empty ones if necessary
        os.renames(os.path.join(d,filename),newtotal) 
        
