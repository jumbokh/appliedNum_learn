## module muller

def muller(f,x1,x2,tol=1.0e-5,kmax):
    logdat = []
    xold = 0
	x3 = (x1+x2)/2
    y1 = f(x1)
    y2 = f(x2)
    y3 = f(x3)
	c1 = (y2-y1)/(x2-x1)
    for i in range(kmax):
  





  
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
