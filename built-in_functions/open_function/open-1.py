with open('OUTCAR','r') as fw:   # open is a function with two arguments: 1st one is file name and 2nd one is mode of operation
    line = fw.readline()         # reads the 0th line of the opened file as a string the whole line
    print(line)                  # prints the 0th line
    sline = line.split()         # splits the whole 0th line as a list of strings
    print(sline)                 # prints the list of strings for 0th line

    line = fw.readline()         # reads the 1st line of the opened file as a string the whole line
    sline = line.split()         # splits the whole 1st line as a list of strings
    print(sline)                 # prints empty list as 1st line does not contain anything

    line = fw.readline()         # reads the 2nd line of the opened file as a string the whole line
    sline = line.split()         # splits the whole 2nd line as a list of strings
    print(sline)                 # prints the list of strings for 2nd line


    lines = fw.readlines()[10]   # reads the 10th line (starting from 0 again) after the 2nd line(read by previous readline())
    print(lines)

#    data = fw.read()           # reads the whole file and store as 'data'
#    print(data)                # prints the whole content of the file opened
    fw.close()                   # closes the file opened


# which line/lines will be read by readline() or readlines() depends on how many readline() or readlines() you have used earlier
