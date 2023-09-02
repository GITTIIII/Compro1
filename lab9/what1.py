print("Using while loop ...")
while(True):
    n = int(input('Enter a number (1-10): '))
    if n<=10 and n>=1 : 
        break
a = 0
if n%2==0 :
    n = n-1
for n in range(n,0,-2) :
        print(n,end=" ")
        a = a+n
print(f"\nSum = {a}")