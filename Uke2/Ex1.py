import numpy as np

"""

Fullfør programmet under.

Du må gjøre ferdig metoden halvering_solve som tar en funksjon f, et intervall [a,b]
 og en toleranse tol, og finner en rot av funksjonen f som har bakoverfeil mindre enn tol.

Programmet skal finne en løsning av ligningen under som er riktig med 6 desimaler.
Du må da definere lambdafunksjonen f og kalle halveringsmetode-funksjonen din med riktig intervall
og toleranseverdi og printe ut roten.

x^3=9

"""

def halvering_solve(f, a,b, tol):
   #Din kode her :) --->
   running = True
   while running:
      c = (a+b)/2
      if f(c) == 0:
         return c

      print(f"f(a) = {f(a)}, f(b) = {f(b)}")
      if f(a)*f(c) < 0:
         b = c
      else:
         a = c
      if np.abs(f(c)) <= tol:
         running = False
   return c

f = lambda x: x**3 - 9 #Hvilken funksjon f er det du skal finne roten av?
maks_feil = 0.0000009#Hva blir maks feil om x_sol skal være riktig med minst 6 desimaler?
x_sol = halvering_solve(f,2,3, maks_feil) #Hva må startintervallet være?
print(x_sol)
