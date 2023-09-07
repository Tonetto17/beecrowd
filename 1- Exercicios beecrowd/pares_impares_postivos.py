A= int(input())
B= int(input())
C= int(input())
D= int(input())
E= int(input())
par = 0
impar = 0
positivos = 0
negativos = 0
if A%2 == 0:
    par+=1
else:
    impar+=1
if A>0:
    positivos+=1
elif A<0:
    negativos+=1
if B%2 ==0:
    par+=1
else:
    impar+=1   
if B>0:
    positivos+=1
elif B<0:
    negativos+=1
if C%2 ==0:
    par+=1
else:
    impar+=1   
if C>0:
    positivos+=1
elif C<0:
    negativos+=1
if D%2 ==0:
    par+=1
else:
    impar+=1   
if D>0:
    positivos+=1
elif D<0:
    negativos+=1
if E%2 ==0:
    par+=1
else:
    impar+=1   
if E>0:
    positivos+=1
elif E<0:
    negativos+=1
print(par, "valor(es) par(es)")
print(impar, "valor(es) impar(es)")
print(positivos, "valor(es) positivo(s)")
print(negativos, "valor(es) negativo(s)")




