from gaussJordan import *

mtx = [[3,-1,2],
       [1,1,2],
       [2,-2,-1]]
if gaussJordan(mtx):
  print(mtx)
else:
  print("Singular!")
 