import numpy as np

def LUfactorize(A):
   n,m = np.shape(A)
   L = np.eye(n)
   U = np.zeros((n,n))
   U = A.copy()
   for j in range(n-1):
      for i in range(j+1,n):
         if ( U[j,j] == 0 ): #0 i pivot element
            raise np.linalg.LinAlgError("Zero pivot encountered")
            return 
         mult = U[i,j]/U[j,j]
         U[i,j]=0.0
         L[i,j] = mult
         for k in range(j+1,n):
            U[i,k] = U[i,k] - (U[j,k]*mult)
   return L,U

   
def LUsolve(L,U,b):

   c = np.zeros_like(b)
   n = len(c) 
   for i in range(n):
      c[i] =b[i]
      for j in range(i):
         c[i] = c[i] - L[i,j]*c[j]
   
   x = c.copy()
   for i in range(n-1,-1,-1):
      for j in range(i+1,n):
         x[i] = x[i] - U[i,j]*x[j]
      x[i] = x[i]/U[i,i]
   
   return x

A = np.array([3.0,1.0,2.0,6.0,3.0,4.0,3.0,1.0,5.0])
A = A.reshape((3,3))
b = np.array([0.0,1.0,3.0]).T
try:
   L,U = LUfactorize(A)
   x = LUsolve(L,U,b)
   print(x) # Fjern ved innlevering
except np.linalg.LinAlgError as e:
   print(f"LinAlgError: {e}")

