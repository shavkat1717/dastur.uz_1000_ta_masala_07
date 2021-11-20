n=int(input("n > 0 butun sonni kiriting: n => "))
import math
if n>0:
    k=0
    s=0
    l=0
    while n>0:
        k=n%10
        s=s+k
        n=math.floor(n/10)
        l=l+1
    print(f"Ushbu sonning raqamlari yig'indisi: {s} ga teng,\nRaqamlari soni esa {l} ta.")    
else:
    print("n > 0 shartga e'tibor bering!")