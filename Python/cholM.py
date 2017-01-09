#!/usr/bin/env python # cholM.py

#Cholesky factor
import numpy as np
import sys

def cholR(A):
	if A.shape == (1,1):
		if A[0][0] < 0: 
			raise ValueError('Matrix is not positive definite') 
		return np.sqrt(A)
	chol = np.empty(A.shape, 'float64')
	alpha = A[0][0]
	if alpha < 0: 
		raise ValueError('Matrix is not positive definite') 
	b = A[1:, 0]
	bt = b.transpose()
	c = A[1:, 1:]

	alpha_sqrt = np.sqrt(alpha)
	chol[0][0] = alpha_sqrt
	chol[1:, 0] = b/alpha_sqrt
	chol[0, 1:] = 0
	chol[1:, 1:] = cholR(c - np.outer(b,bt)/alpha)
	return chol

def chol(A):
	chol = A.copy()
	counter = 0
	while (1):
		alpha = chol[counter][counter]
		if alpha < 0: 
			raise ValueError('Matrix is not positive definite') 
		alpha_sqrt = np.sqrt(alpha)
		chol[counter][counter] = alpha_sqrt
		if chol.shape == (1,1):
			return chol
		chol[counter, counter+1:] = 0.
		chol[counter+1:, counter+1:] = chol[counter+1:, counter+1:] - np.outer(chol[counter+1:, counter],chol[counter+1:, counter])/alpha
		chol[counter+1:, counter] = chol[counter+1:, counter]/alpha_sqrt
		if chol[counter+1:, counter+1:].shape == (1,1): 
			if chol[-1][-1] < 0: 
				raise ValueError('Matrix is not positive definite') 
			chol[-1][-1] = np.sqrt(chol[-1][-1])
			break
		counter += 1
	return chol

if __name__ == "__main__":
	M = np.array([[25, 15, -5], [15, 18, 0], [-5, 0, 11]])
	N = np.array([[4, 12, -16], [12, 37, -43], [-16, -43, 98]])
	try:
		print(cholR(M))
		print(chol(M))
	except ValueError:
		print('Exception: Nonpositive square root')	

	n = 13
	A = 1./np.add.outer(np.arange(n), np.arange(1., n+1))
	G1 = cholR(A)
	res = np.amax(abs(G1 @ G1.T - A[:n,:n]))
	print("Residual for n = %d is" % n, res)
	if res<10**(-15):
	    print("test1 is passed.")
	else:
	    print("test1 is failed. Residual is too large")

	n = 14
	A = 1./np.add.outer(np.arange(n), np.arange(1., n+1))
	try:
	    G2 = cholR(A[:n,:n])
	    print("No error message when the matrix is not positive definite")
	    print("test2 is failed")
	except Exception as inst:
	    print(inst)
	    print("test2 is passed")

	n = 13
	A = 1./np.add.outer(np.arange(n), np.arange(1., n+1))
	G3 = chol(A)
	res = np.amax(abs(G3 @ G3.T - A[:n,:n]))
	print("Residual for n = %d is" % n, res)
	if res<10**(-15):
	    print("test3 is passed.")
	else:
	    print("test3 is failed. Residual is too large")

	n = 14
	A = 1./np.add.outer(np.arange(n), np.arange(1., n+1))
	try:
	    G4 = chol(A[:n,:n])
	    print("No error message when the matrix is not positive definite")
	    print("test4 is failed")
	except Exception as inst:
	    print(inst)
	    print("test4 is passed")



