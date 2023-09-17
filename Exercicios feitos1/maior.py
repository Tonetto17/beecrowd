A, B, C=map(int, input().split())
MaiorAB=(A+B+abs(A-B))/2
if MaiorAB>=C:
    print(f'{MaiorAB:.0f} eh o maior')
else:
    print(f'{C:.0f} eh o maior')
