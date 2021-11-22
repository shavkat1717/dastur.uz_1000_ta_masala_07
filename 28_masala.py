n=float(input("Istalgan n sonini kiriting: n => "))
if n>0:
    import math
    a=2
    b=2+1/a
    x=math.fabs(b-a)
    k=2
    while x>=n:
        a=b
        b=2+1/a
        x=math.fabs(b-a)
        k=k+1
    print(x)
    print(k)   
else:
    print("Diqqat xato. Shartga qarang: Musbat son kiriting!")