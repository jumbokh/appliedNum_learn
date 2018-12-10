
np.set_printoptions(precision=4, suppress=True)
A = np.array([[6, 5, 0],[5, -1, 4],[5, 1, -14],[0, 4, 3]],dtype=float)

(Q, R) = gram_schmidt(A)
print(Q)
print(R)
print np.dot(Q,R)

(Q, R) = givens_rotation(A)
print(Q)
print(R)
print np.dot(Q,R)

(Q, R) = householder_reflection(A)
print(Q)
print(R)
print np.dot(Q,R)
#--------------------- 
#作者：team79 
#来源：CSDN 
#原文：https://blog.csdn.net/hzh_0000/article/details/78655725 
#版权声明：本文为博主原创文章，转载请附上博文链接！