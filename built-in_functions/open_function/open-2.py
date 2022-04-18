file=input('enter the file name\n')
with open(file,'r') as fw:      # Here file is a variable
    data = fw.read()            # reads the whole file and store as 'data'.
    print(data)                 # prints the whole content of the file opened
    fw.close()                  # closes the file opened
