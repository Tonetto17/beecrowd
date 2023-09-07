N= int(input())
F= 10
AS=7
total= AS
if N>F:
    if N<=30:
        total+=(N-F)*1
    elif N<=100:
        total+= 20+(N-30)*2
    else:
        total+= 20+140+(N-100)*5
print(total)