So=float(input("Bankka qo'yilgan boshlang'ich summani kiriting: So => "))
p=int(input("Har oyda qo'shiladigan 0 < p < 25 foizni kiriting: p => "))
if So>0 and 0<p<25:
    S=So
    k=0
    while S<2*So:
        S=S+S*p/100
        k=k+1
    print(k)    
else:
    print("So > 0 va 0 < p < 25 shartga e'tibor bering!")