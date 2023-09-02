print("Using while loop to add only positive number form 6 input...")
n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))
n3 = int(input("Number 3: "))
n4 = int(input("Number 4: "))
n5 = int(input("Number 5: "))
n6 = int(input("Number 6: "))
n = (n1,n2,n3,n4,n5,n6)
i = 0

while(True) :
    for x in n :
        if x < 0 :
            continue
        i = i+x  
    else : break
print(f"Sum of all positive number is {i}.")