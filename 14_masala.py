n=int(input("n > 1 natural sonni kiriting: n => "))
if n>1:
    s=0
    t=1
    while s<n:
        s=s+1/t
        t=t+1
    print(t-2)    
else:
    print("n > 1 shartga e'tibor bering!")