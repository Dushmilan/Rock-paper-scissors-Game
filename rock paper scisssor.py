
x= input("payer-1 (R)ock or (P)aper or (S)cissor?").upper
y=input("payer-2 (R)ock or (P)aper or (S)cissor?").upper
r='R'
s='S'
p='P'
q= 'Palyer 1 wins'
d= 'player 2 wins'
if x==y:
    print("Retry")
elif x==r and y==s or x==p and y== r or x==s and y== p:
    print("player 1 wins")
else:
    print("player 2 wins")