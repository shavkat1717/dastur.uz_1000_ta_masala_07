n=int(input("N > 0 natural sonini kiriting N => "))
if n>0:
    k=n
    while (pow(3,k)>n):
        k=k-1
    print(k)
else:
    print("N > 0 shartiga e'tibor bering!")