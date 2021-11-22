a=int(input("Birinchi sonni kiriting: => "))
b=int(input("Ikkinchi sonni kiriting: => "))
while a!=b:
    if a>b:
        a=a-b        
    else:   
        b=b-a;        
print('Bu sonlarning EKUBi = ',a);