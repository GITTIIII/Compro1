a = int(input("How many customer?: "))
b = int(input("How much per head?: "))
c = a//4
print("Total payment for",a,"customers is","%.0f"%((a-c)*b),"baht.")