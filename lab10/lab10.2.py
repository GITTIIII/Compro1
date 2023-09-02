print("Using continue !!!")
s = "suranaree"
i = ""
i1 = ""

for x in range(1,21) :
    if x%3==0 : 
        i = i+str(x)+" "
    else : continue

for w in s :
    if w == "a" :
        continue
    else : i1 = i1+w+" "
print(i)
print(i1)