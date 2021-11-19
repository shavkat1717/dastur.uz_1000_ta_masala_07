n=int(input("A sonini kiriting A => "))
if n>0:
    p=1
    while (n>=2):
        p=p*n
        n=n-2
    print(p)
else:
    print("A > 0 shartiga e'tibor bering! ")