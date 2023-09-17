N = float(input(''))
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
resultado = []
for x in notas:
    quant = int(N / x)
    resultado.append(quant)
    N = round(N - quant * x, 2)  
for z in moedas:
    Q = int(N / z)
    resultado.append(Q)
    N = round(N - Q * z, 2)  
print('NOTAS:')
print(f'{resultado[0]} nota(s) de R$ {notas[0]}.00')
print(f'{resultado[1]} nota(s) de R$ {notas[1]}.00')
print(f'{resultado[2]} nota(s) de R$ {notas[2]}.00')
print(f'{resultado[3]} nota(s) de R$ {notas[3]}.00')
print(f'{resultado[4]} nota(s) de R$ {notas[4]}.00')
print(f'{resultado[5]} nota(s) de R$ {notas[5]}.00')
print('MOEDAS:')
print(f'{resultado[6]} moeda(s) de R$ {moedas[0]:.2f}')
print(f'{resultado[7]} moeda(s) de R$ {moedas[1]:.2f}')
print(f'{resultado[8]} moeda(s) de R$ {moedas[2]:.2f}')
print(f'{resultado[9]} moeda(s) de R$ {moedas[3]:.2f}')
print(f'{resultado[10]} moeda(s) de R$ {moedas[4]:.2f}')
print(f'{resultado[11]} moeda(s) de R$ {moedas[5]:.2f}')
