N= int(input())
for I in range(N):
    V=int(input())
    if V==0:
        print("NULL") 
    elif V%2==0:
        print("EVEN", end=" ")
    else:
        print("ODD", end=" ")
    if V>0:
        print("POSITIVE")
    elif V<-1:
        print("NEGATIVE")
   
        
        

