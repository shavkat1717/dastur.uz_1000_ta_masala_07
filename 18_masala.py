n=int(input("n > 0 butun sonni kiriting: n => "))
import math
if n>0:
    k=0
    while n>0:
        k=n%10
        print(k,end=(""))
        n=math.floor(n/10)
else:
    print("n > 0 shartga e'tibor bering!")