while(True) :
    W = int(input("Width (7-10): "))
    if W<7 or W>10 :
        print("Invalid Number!")
    else : break

while(True) :
    B = int(input("Border (1-3): "))
    if B<1 or B>3 :
        print("Invalid Number!")
    else : break

for x in range(1, W+1) :
        for i in range(1, W+1) :
            if (x<=B or i<=B or x>W-B or i>W-B) :
                print("*",end="")
            else:
                print(" ",end="") 
        print()