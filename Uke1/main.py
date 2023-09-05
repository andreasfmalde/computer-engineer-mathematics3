import numpy as np

"""
def nest(c,x):
	lengde = len(c)
	y = c[-1]
	for i in range(lengde-2,-1,-1):
		y = y * x + c[i]
		print(i)
		print(y)

	print(y)



nest([-1,5,-3,3,2],1/2)
print(469/81)
"""

# Oppgave 11
a = 3344556600.0
b = 1.2222222
result = b**2/(np.sqrt(a**2+b**2)+a)
result = "{:.5e}".format(result)
print(result)