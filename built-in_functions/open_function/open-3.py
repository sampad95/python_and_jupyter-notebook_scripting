with open('EIGENVAL','r') as fw:    

#    lines = fw.readlines()[0:5]  # reads five lines (0th to 4th)
#    print(lines)                 # prints the five lines as list of strings, each line as a string

    line5 = fw.readlines()[5]    # reads the 5th line counting starts from 0
    print(line5)                 # prints the 5th line counting starts from 0
    sline5 = line5.split()
    print(sline5)

    nelect = int(sline5[0])      # 0th element of the list  # int() is another built-in function converts string to integer
    nkpt = int(sline5[1])        # 1st element of the list
    nband = int(sline5[2])       # 2nd element of the list
    print('number of electrons =',nelect)
    print('number of kpoints =',nkpt)
    print('number of bands =',nband)

#    data = fw.read()             # reads the whole file and store as 'data'.
#    print(data)                  # prints the whole content of the file opened
    fw.close()                   # closes the file opened
