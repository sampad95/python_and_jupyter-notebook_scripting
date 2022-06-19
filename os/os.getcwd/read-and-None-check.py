import os
fnr=None                                                   #defines fnr as None
parentdir=os.getcwd()
destfile='write-in-file.py'
if (parentdir!=None) and (destfile!=None):                 #whether parentdir and destfile exist or not
    destination_file=os.path.join(parentdir,destfile)      #joins the present path with the file
    if os.path.isfile(destination_file):                   #checks the file destination after joining path exists in that path
        fnr=open(destfile,'r')                             #fnr gets value 
        print('"write-in-file.py" file found')             #prints if "destination_file" path is true
else:
    destination_file=None                                  #defines destination_file as None if "destination_file" not found
if fnr==None:                                   #asks fnr is None, true and then for the answer true prints the next.
    print('could not find "write-in-file.py"')  #prints if "write-in-file.py" file does not exist in the present directory
