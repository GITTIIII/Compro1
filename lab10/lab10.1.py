print("Using break !!!")
s = "suranaree"
i = ""
i1 = ""

while(True) :
    for x in range(1,21) :
        if x<=7 : 
            i = i+str(x)+" "
    break

while(True) :
    for w in s :
        if w != "n" :
            i1 = i1+w+" "
        elif w == "n" :
            i1 = i1+w
            break
    break
print(i)
print(i1)