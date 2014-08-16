"""
Takes Dad's backup files in Windows format blahfolder\blahfolder\blahfile.extension and puts it into
Mac OS X format blahfolder/blahfolder/blahfile.extension
"""

import os

for d,s,f in os.walk("/Users/Jenna/Desktop/Dad's backups from 2012-10-14"):
    for filename in f:
        if filename[0] == '.':
            continue
##        print filename
        newname = '/'.join(filename.split('\\')).replace('C/Users/HECaldwell/','')
        newnamelist = newname.split('/')
##        print newnamelist
        newpath =  d+'/'+'/'.join(newnamelist[:-1])
        newfile = newnamelist[-1]
        print newpath+'/'+newfile
        if not os.path.exists(newpath):  ##note: because I'm using os.renames instead of os.rename below, I probably don't need this
            os.makedirs(newpath)
        if "Zone.Identifier" in newfile:
            os.renames(d+'/'+filename,newpath+'/probably junk files/'+newfile)
        else:
            os.renames(d+'/'+filename,newpath+'/'+newfile) 
        
