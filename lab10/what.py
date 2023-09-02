n = 3,6,9,12,15
print('Using "break" ...')
print(str(n).replace(","," ").replace("(","").replace(")",""))
i = 0
for x in n :
    i = i+x
print(f"Sum of all numbers is {i}.")
print("End Program !!!")