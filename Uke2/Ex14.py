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


# Resten av koden kan du la stå som den er :)   
A = np.array([ 1.0,  2,-1,0,3,1,2,-1,1 ]) #Prøv å skrive "1.0" som "1" - Hva foregår?
A=A.reshape((3,3))
try:
   L,U = LUfactorize(A)
   print(L) # Fjern ved innlevering
   print(U) # Fjern ved innlevering
except np.linalg.LinAlgError as e:
   print(f"LinAlgError: {e}")
