print("Displays prime numbers from 1 to N.")
n = int(input("Please enter a value of n: "))
prime = ""
for x in range(0,n):
    if x>=1:
        for i in range(2,x):
            if x%i==0:
                break
        else:
            prime = prime+str(x)+" "
print(f"They are {prime}")