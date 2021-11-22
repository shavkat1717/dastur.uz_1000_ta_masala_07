n=float(input("Istalgan n sonini kiriting: n => "))
if n>0:
    import math
    a=1
    b=2
    c=(a+2*b)/3
    x=math.fabs(b-a)
    k=3
    while x>=n:
        a=b
        b=c
        c=(a+2*b)/3
        x=math.fabs(b-a)
        k=k+1
    print(x)
    print(k)   
else:
    print("Diqqat xato. Shartga qarang: Musbat son kiriting!")