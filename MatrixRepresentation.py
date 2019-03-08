import sys
#Matricies given in the file must be on just one line for this to work
def getData(path):
    '''
    Converts the data from the file into useable matricies
    If the matrix is like the one given as an example but not in the correct order, it will put it in the correct order
    '''
    #Each line of a file is a matrix
    f = [line for line in open(path, 'r')]
    #Iterates over each matrix, splitting it up into arrays which just contain [a,b,weight]
    data = []
    for matrix in f:
        #Splits each line on the opening square bracket
        matrix = matrix.split('[')
        m = []
        for element in matrix:
            e = []
            for char in element:
                #Removes all useless characters except commas as these are used to separate items in each element
                if char!="'" and char!="]" and char!=' ' and char!='\n':
                    e.append(char)
            #Turns e into an array containing [a,b,weight]
            e = ''.join(e)
            e = [i for i in e.split(',') if i!='']
            #Checks for empty arrays and removes from the new matrix if present
            if e!=[]:
                m.append(e)
        #By sorting the matrix, each column is grouped together - allowing matrices to be given in any order
        m.sort()
        data.append(m)
    return data

def getN(data, index):
    '''Counts the number of times which the first element occurs and so the value of n for the matrix'''
    matrix = data[index]
    n = 0
    firstElement = matrix[0][0]
    for element in matrix:
        if element[0]==firstElement:
            n+=1
    return n

def displayTables(data):
    '''Iterates over all of the matricies stored in the file, printing out the table of weights for each'''
    for index in range(len(data)):
        #Gets the value of n for each n*n matrix
        N = getN(data, index)

        #Sets the current matrix to be displayed
        matrix = data[index]
        #Generates the header for the table and prints it
        header = [matrix[e][0] for e in range(len(matrix)) if e%N==0]
        print('        ', end=' | ')
        for i in header:
            print(i, end=' | ')
        print()
        for r in range(1, N+1):
            #Gets the name of the row using the header
            name = header[r-1]
            #Gets the weights for this row
            row = [matrix[e][2] for e in range(N*(r-1),len(matrix)) if e<(N*r)]
            #Inserts the name at the start of the row
            row.insert(0,name)
            #Iterates over the row, printing it
            for i in row:
                print(i, end=' |        ')
            print()
        print()

'''
def HTMLTable(data):
    f = open('Table.HTML', 'w+')
    f.write('<TABLE cellpadding="4" style="border: 1px solid #000000; border-collapse: collapse;" border="1">')
    for index in range(len(data)):
        #Gets the value of n for each n*n matrix
        N = getN(data, index)

        #Sets the current matrix to be displayed
        matrix = data[index]
        #Generates the header for the table and prints it
        header = [matrix[e][0] for e in range(len(matrix)) if e%N==0]
        header.insert(0,'        ')
        f.write('<TR>')
        for i in header:
            line = '<TH>'+i+'</TH>'
            f.write(line)
        f.write('</TR>')
        for r in range(1, N+1):
            f.write('</TR>')
            #Gets the name of the row using the header
            name = header[r-1]
            #Gets the weights for this row
            row = [matrix[e][2] for e in range(N*(r-1),len(matrix)) if e<(N*r)]
            #Inserts the name at the start of the row
            row.insert(0,name)
            for i in row:
        '''



if __name__=='__main__':
    #Iterates over all of the paths given as arguments, displaying the tables for each
    #sys.argv starts at the name of the python script when running from terminal using 'python MatrixRepresentation.py <file>'
    for i in range(1, len(sys.argv)):
        path = sys.argv[i]
        try:
            #Checks if the path contains a file
            open(path, 'r')
            #If it does then continues the program
            displayTables(getData(path))
        except FileNotFoundError:
            #If it doesnt exist then print an error and dont run
            print('No such file: ', path)
