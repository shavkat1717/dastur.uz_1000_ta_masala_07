n=int(input("n > 1 son kiriting: n => "))
idf=0
if n>1:
    for x in range(2,n):
        if(n%x)==0:
            idf=1
        else:
            pass
    if idf==0:
        print("Siz kiritgan son tub!")
    elif idf==1:
        print("Siz kiritgan son tub emas. Ya'ni murakkab son!")
else:
    print("n > 1 shartiga e'tibor bering!")