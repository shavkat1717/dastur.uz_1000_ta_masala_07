a=int(input("a > 1 natural sonni kiriting: a => "))
if a>1:
    s=0
    t=1
    while s<a:
        s=s+1/t
        t=t+1
    print(t-1)    
else:
    print("a > 1 shartga e'tibor bering!")