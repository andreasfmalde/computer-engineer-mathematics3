import numpy as np

def LUfactorize(A):
   n,m = np.shape(A)
   L = np.eye(n)
   U = np.zeros((n,n))
   U = A.copy()
   for j in ?????:
      for i in range(?????):
         if ( ???? ): #0 i pivot element
            raise np.linalg.LinAlgError("Zero pivot encountered")
            return 
         mult = ?????
         U[i,j]=0.0
         L[i,j] = ????
         for k in range(???, ???):
            U[?,?] = ?????
   return L,U

   
def LUsolve(L,U,b):

   c = np.zeros_like(b)
   n = len(c) 
   for i in ????:
      c[i] =b[i]
      for j in ????
         c[i] = c[i] - ??????
   
   x = c.copy()
   for i in ?????:
      for j in ??????:
         x[i] = ?????
      x[i] = ?????
   
   return x

A = ????
b = ???
try:
   L,U = LUfactorize(A)
   x = LUsolve(L,U,b)
except np.linalg.LinAlgError as e:
   print(f"LinAlgError: {e}")

