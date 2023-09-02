print("Printing 1 to 9 using for loop ...")
for n in range(1,10) : 
    if n<8 :
        print(str(n)+", ",end=" ")
    if n==8 :
        print(str(n),"and",end=" ")
    elif n==9 :
        print(str(n)+".")
print("End Program !!!")