x1,y1=map(float, input().split())
x2,y2=map(float, input().split())
conta=((x2-x1)**2)+((y2-y1)**2)
distancia=conta**(1/2)
print(f'{distancia:.4f}')