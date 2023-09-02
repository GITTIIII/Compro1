while(True):
    n = int(input('Enter a number (2-10): '))
    if n<=10 and n>=2 : 
        break
    else : print("Invalid Number!")
a = 0
b = 1
c = 0
print("Fibonacci sequence up to 10 :",end=" ")
while c<n :
    print(a,end=" ")
    d = a+b
    a = b
    b = d
    c = c+1