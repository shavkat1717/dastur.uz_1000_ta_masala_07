n=int(input("n > 1 son kiriting: n => "))
if n>1:
    a=1
    b=1
    c=0
    while c<n:
        c=a+b
        a=b
        b=c
        if a+c>n:
            print(c+a)
            break
else:
    print("Diqqat xato. Shartga qarang: n > 1 son kiriting!")