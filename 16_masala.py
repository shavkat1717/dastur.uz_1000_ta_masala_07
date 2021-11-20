print("\nSportchi birinchi kuni 10 km yugurdi!")
p=int(input("Har kungi qo'shiladigan 0 < p < 50 foizni kiriting: p => "))
if 0<p<50:
    S=10
    k=0
    while S<200:
        S=S+S*p/100
        k=k+1
    print(k+1)    
else:
    print("0 < p < 50 shartga e'tibor bering!")