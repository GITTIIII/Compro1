n = int(input("Enter a number 100-999: "))
a = n//100
b = (n//10)%10
c = n%10
d = a+b+c
print(n,"is separated to",str(a)+",",b,"and",str(c)+".")
print("Sum of",str(a)+",",b,"and",c,"is",str(d)+".")