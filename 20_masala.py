n=int(input("n > 0 butun sonni kiriting: n => "))
import math
if n>0:
    k=0
    while n>0:
        k=n%10
        if k==2:
            print("Berilgan sonning raqamlari orasida 2 bor.")
            break
        n=math.floor(n/10)
    if n==0:
        print("Berilgan sonning raqamlari orasida 2 yo'q")
else:
    print("n > 0 shartga e'tibor bering!")