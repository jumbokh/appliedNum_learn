## module secant

def secant(f,x0,x1,n,tol=1.0e-5):
    xold = 0
    for i in range(n):
      print(i,'{0:8.6f}'.format(x0),'{0:8.6f}'.format(x1),'{0:8.6f}'.format(f(x1)))  
      if f(x1)-f(x0) == 0:
         return x1       
      x_temp = x1 - (f(x1)*(x1-x0)*1.0)/(f(x1)-f(x0))
      y_temp = f(x_temp)
      if abs(y_temp) < tol*max(abs(x1),1.0): 
         return x1
      xold = x_temp
      x0 = x1
      x1 = x_temp
       
    return x1
