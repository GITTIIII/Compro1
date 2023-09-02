print("Printing 1 to 9 using for loop ...")
print('Using "pass", if the number is odd and greater than 5')
i = ""
for x in range(1,10) :
    if x>5 :
        if x%2==0 :
             i = i+str(x)+" "
        else : pass
    else : i = i+str(x)+" "
print(i)
print("End Program!!!")