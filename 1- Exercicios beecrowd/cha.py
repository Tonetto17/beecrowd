# Lê o tipo de chá real
T= int(input())
A, B, C, D, E=map(int, input().split())
resp= 0
if(A==T):
    resp+=1
if(B==T):
    resp+=1
if(C==T):
    resp+=1
if(D==T):
    resp+=1
if(E==T):
    resp+=1
print(resp)