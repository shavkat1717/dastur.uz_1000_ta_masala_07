A=int(input("To'g'ri to'rtburchakning enini kiriting: A = "))
B=int(input("To'g'ri to'rtburchakning bo'yini kiriting: B = "))
C=int(input("Kvadratning tomonini kiriting: C = "))
import math
x=math.floor(A/C)
y=math.floor(B/C)
n=x*y
Sq=A*B-n*C**2
print(f"Mazkur to'g'ri to'rtburchakning ichiga {n} ta kvadratni joylashtirish mumkin, Qoldiq yuza {Sq} ga teng!")

# a=int(input("A butun musbat sonni kiriting: A = "))
# b=int(input("B butun musbat sonni kiriting: B = "))
# c=int(input("C butun musbat sonni kiriting: C = "))
# l=0
# import math
# while c**2<=a*b:
#     n=math.fabs((a*b)/c**2)
#     l=l+1
#     break
# print(f"Tomonlari {a} va {b} bo'lgan to'rtburchak ichiga tomoni {c} bo'lgan kvadratdan {l} ta joylashtirish mumkin.")