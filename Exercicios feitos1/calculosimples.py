linha1=input().split()
linha2=input().split()
A, B, C=map(float, linha1)
D, E, F=map(float, linha2)
aa=B*C
bb=E*F
final=aa+bb
print(f'VALOR A PAGAR: R$ {final:.2f}')