n = input("Enter a 8-bit binary number: ")
n1 = n[-7:-9:-1][::-1]
n2 = n[-4:-7:-1][::-1]
n3 = n[-1:-4:-1][::-1]
a = int(n1[-2])*2+int(n1[-1])*1
b = int(n2[-3])*4+int(n2[-2])*2+int(n2[-1])*1
c = int(n3[-3])*4+int(n3[-2])*2+int(n3[-1])*1

print(n,"=",n1,n2,n3)

print("%8s"%n1,"=",str(n1[-2])+"*(2**1)+"+str(n1[-1])+"*(2**0) =",a)

print("%8s"%n2,"=",str(n2[-3])+"*(2**2)+"+str(n2[-2])+"*(2**1)+"+str(n2[-1])+"*(2**0) =",b)

print("%8s"%n3,"=",str(n3[-3])+"*(2**2)+"+str(n3[-2])+"*(2**1)+"+str(n3[-1])+"*(2**0) =",c)

print(n,"=",str(a)+str(b)+str(c))