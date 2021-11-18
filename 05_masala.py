a=int(input("A sonini kiriting A => "))
if a>0:
    p=0
    while (a>=2):
        a=a/2
        p=p+1
    print(f"Ushbu son 2 ning {p}-darajasi.")
else:
    print("A > 0 shartiga e'tibor bering!")