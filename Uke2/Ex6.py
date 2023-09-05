import numpy as np

# EXpected : 2.0201
#---------> Kod i vei
volum = 60
høyde = 10
f = lambda x: x**3 + 5*x**2-(90/np.pi) 
df = lambda x: 3*x**2 + 10*x
tol = 0.00009

def newton(f,df,x0,tol):
	while True:
		x = x0 - (f(x0)/df(x0))
		if np.abs(x-x0) <= tol:
			return x
		x0 = x

#<--------------
radius = newton(f,df,3,tol) #La variabelen radius holde svaret ditt
print(radius)