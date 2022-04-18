file=input('enter the file name\n')
with open(file,'r') as fw:      # Here file is a variable

#    lines = fw.readlines()[0:5]  # reads five lines (0th to 4th)
#    print(lines)                 # prints the five lines as list of strings, each line as a string


    print(fw.readlines()[5])     # reads and prints the 5th line counting starts from 0

#    data = fw.read()             # reads the whole file and store as 'data'.
#    print(data)                  # prints the whole content of the file opened
    fw.close()                   # closes the file opened
