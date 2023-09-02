a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
if (a>c and a<b) : d=a
elif (b>c and b<a) : d=b
else : d=c
print("The middle number of",str(a)+", "+str(b)+" and "+str(c)+" is "+str(d)+".")