N=int(input(''))
cedulas=[100, 50, 20, 10, 5, 2, 1]
cont=0
print(N)
for i in range(len(cedulas)):
    cont=N//cedulas[i]
    N%=cedulas[i]
    print(f'{cont} nota(s) de R$ {cedulas[i]},00')
