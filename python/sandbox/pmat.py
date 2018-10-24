def pmat(matrix):
    size = len(matrix[0])
    #print(size)
    print()
    for a in matrix:
        for i in range(size):
            #print("%+d"%round(a[i],2),end="")
            number = round(a[i],2)
            print('{0: .2f}'.format(number, '-' if number else ' '),'  ',end='')
	
            if i < size-1 :
              print(", ",end="")
        print()