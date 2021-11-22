n=int(input("Fibonachchi sonlari ketma-ketligi orasidan  son kiriting: n => "))
if n>0:
    a=1
    b=1
    c=0
    l=2
    while c<n:
        c=a+b
        a=b
        b=c
        l=l+1
    if n==c:
        print(f"Ushbu son {l}-had hisoblanadi.")
    elif n==1:
        print("Ushbu son ham 1-had, ham 2-had hisoblanadi.")
    else:
        print("Ushbu son fibonachchi sonlari ketmaketligiga kirmaydi.")
else:
    print("Diqqat xato. Shartga qarang: Musbat son kiriting!")