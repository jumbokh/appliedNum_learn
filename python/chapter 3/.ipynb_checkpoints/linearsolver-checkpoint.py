{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "### module linearsolver\n",
    "\n",
    "def linearsolver(A,b):\n",
    "  n = len(A)\n",
    "  M = A\n",
    "\n",
    "  i = 0\n",
    "  for x in M:\n",
    "   x.append(b[i])\n",
    "   i += 1\n",
    "\n",
    "  for k in range(n):\n",
    "   for i in range(k,n):\n",
    "     if abs(M[i][k]) > abs(M[k][k]):\n",
    "        M[k], M[i] = M[i],M[k]\n",
    "     else:\n",
    "        pass\n",
    "\n",
    "   for j in range(k+1,n):\n",
    "       q = float(M[j][k]) / M[k][k]\n",
    "       for m in range(k, n+1):\n",
    "          M[j][m] -=  q * M[k][m]\n",
    "\n",
    "  x = [0 for i in range(n)]\n",
    "\n",
    "  x[n-1] =float(M[n-1][n])/M[n-1][n-1]\n",
    "  for i in range (n-1,-1,-1):\n",
    "    z = 0\n",
    "    for j in range(i+1,n):\n",
    "        z = z  + float(M[i][j])*x[j]\n",
    "    x[i] = float(M[i][n] - z)/M[i][i]\n",
    "  print (x)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.5.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
