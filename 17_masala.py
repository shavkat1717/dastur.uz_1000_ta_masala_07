n=int(input("n > 0 butun sonni kiriting: n => "))
m=int(input("m > 0 butun sonni kiriting: m => "))
if n>m>0:
    k=0
    while n>m:
        n=n-m
        k=k+1
    print(k)
    print(n)
else:
    print("n > m > 0 shartga e'tibor bering!")