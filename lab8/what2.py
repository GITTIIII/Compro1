n = input("Enter a number (100-999): ")
a = int(n[0])
b = int(n[1])
c = int(n[2])
if (a>b and a>c) : print("The biggest number is",a)

elif (b>a and b>c) : print("The biggest number is",b)

else : print("The biggest number is",c)