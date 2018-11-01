## module newton

def newtonx(f,fpr,x,n,tol=1.0e-5):
    logdat = []
    xold = 0
    for i in range(n):
       
      if f(x)-f(xold) == 0:
         return x,logdat
      y = f(x)
      ypr = fpr(x)	  
      x_temp = x - y/ypr
      y_temp = f(x_temp)
      logdat.append([x,y,x_temp,y_temp])
      #print(i,'{0:8.6f}'.format(x),'{0:8.6f}'.format(x_temp),'{0:8.6f}'.format(y)) 
      if abs(x_temp-x) < tol: 
         return x,logdat
      xold = x
      x = x_temp
    return x,logdat
