from gaussJordan import *

mtx = [[3,-1,2],
       [1,1,2],
       [2,-2,-1]]

  
B = inv(mtx)
print(B)

zeros(3)
ans = solve(mtx,B)

if ans != None:
  print(ans)
else:
  print("Singular!")