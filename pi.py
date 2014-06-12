'''
Pythagoras (Chicot) method for aproximating pi
'''
from decimal import Decimal

# Given the n-th approximation, q, of pi**2
# it computes the (n+1)-approximation 
def chicot(n,q):
    p = 2**(2*n)
    return Decimal(1)*(q + p*(1-(1-q/p).sqrt())**2)

X=[(2,(Decimal(8)).sqrt())]
z = int(raw_input("Ingresa la cantidad de terminos: "))
for n in range(2,z):
    q=(X[n-2][1])**2
    q=chicot(n,q)
    X=X+[(n+1,q.sqrt())]

for x in X:
    print(x)  
    