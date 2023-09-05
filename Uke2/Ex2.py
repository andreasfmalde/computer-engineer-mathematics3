import numpy as np

def fikspunkt_solve(f, x0,tol):
    while True:
        x = f(x0)
        if np.abs(x-x0) <= tol:
            return x
        x0 = x
    return x

f1 = lambda x: np.cbrt(2*x + 2) #Hvilken funksjon skal inn i fikspunkt_solve? (lign. 1)
f2 = lambda x: np.log(7-x)#Hvilken funksjon skal inn i fikspunkt_solve? (lign. 2)
f3 = lambda x: np.log(4 - np.sin(x)) #Hvilken funksjon skal inn i fikspunkt_solve? (lign. 3)
funcs = [f1,f2,f3]
maks_feil = 0.000000009#????
sols = []
for f in funcs:
   x_sol = fikspunkt_solve(f,1,maks_feil )
   sols.append(x_sol)

print(f"Løsning til første ligning x = {sols[0]}")
print(f"Løsning til andre ligning x = {sols[1]}")
print(f"Løsning til tredje ligning x = {sols[2]}")