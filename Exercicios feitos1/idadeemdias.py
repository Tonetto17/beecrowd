idade=int(input(''))
anos=[365, 30, 1]
resultado=[]
for i in anos:
    quant=int(idade/i)
    resultado.append(quant)
    idade=idade-quant*i  
print(f'{resultado[0]} ano(s)')
print(f'{resultado[1]} mes(es)')
print(f'{resultado[2]} dia(s)')