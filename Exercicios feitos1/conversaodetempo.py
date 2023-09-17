N=int(input(''))
tempo=[3600, 60, 1]
resultado=[]
for i in tempo:
    quant=int((N/i))
    resultado.append(quant)
    N=N-quant*i
print(f'{resultado[0]}:{resultado[1]}:{resultado[2]}')


