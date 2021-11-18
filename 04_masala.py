a=int(input("A sonini kiriting A => "))
if a>0:
    p=1
    while (a>p):
        p=p*3
    if a==p:
        print("Ushbu son 3 ning darajasi.")
    else:
        print("Ushbu son 3 ning darajasi emas.")
else:
    print("A > 0 shartiga e'tibor bering!")