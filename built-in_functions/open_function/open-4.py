with open('EIGENVAL','r') as fw:    
     
    print('nspin = ',int(fw.readlines()[0].split()[-1]))  # in one line  # picks up the element at the position -1 (first one from the right side)

    print('\n')                  # for line spacing
    

    fw.seek(0)                   # moves read cursor to the start( 0th line) of the file
      

    print('number of electrons =',int(fw.readlines()[5].split()[-3]))  # in one line # picks up the element at the position -3  of the list from the right side (starting from position -1)

    fw.seek(0)                   # again moves read cursor to the start( 0th line) of the file

    print('number of kpoints =',int(fw.readlines()[5].split()[-2]))    # in one line # picks up the element at the position -2  of the list from the right side (starting from position -1)

    fw.seek(0)                   # again moves read cursor to the start( 0th line) of the file

    print('number of bands =',int(fw.readlines()[5].split()[2]))       # in one line

    fw.close()                   # closes the file opened
