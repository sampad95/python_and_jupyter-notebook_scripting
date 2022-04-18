with open('OUTCAR','r') as fw:   # open is a function with two arguments: 1st one is file name and 2nd one is mode of operation
    line = fw.readline()         # reads the 1st line of the opened file as a string the whole line
    print(line)                  # prints the 1st line
    sline = line.split()         # splits the whole 1st line as a list of strings
    print(sline)                 # prints the list of strings for 1st line

    line = fw.readline()         # reads the 2nd line of the opened file as a string the whole line
    sline = line.split()         # splits the whole 2nd line as a list of strings
    print(sline)                 # prints the list of strings for 2nd line

    line = fw.readline()         # reads the 3rd line of the opened file as a string the whole line
    sline = line.split()         # splits the whole 3rd line as a list of strings
    print(sline)                 # prints the list of strings for 3rd line


#    data = fw.read()           # reads the whole file and store as 'data'
#    print(data)                # prints the whole content of the file opened
    fw.close()                   # closes the file opened
