## module newton

def newton(f,fpr,x,n,tol=1.0e-5):
    xold = 0
    for i in range(n):
       
      if f(x)-f(xold) == 0:
         return x
      y = f(x)
      ypr = fpr(x)	  
      x_temp = x - y/ypr
      y_temp = f(x_temp)
      print(i,'{0:8.6f}'.format(x),'{0:8.6f}'.format(x_temp),'{0:8.6f}'.format(y)) 
      if abs(x_temp-x) < tol: 
         return x
      xold = x
      x = x_temp
    return x
