t1 = input("Time in: ")
t2 = input("Time out: ")
if t2[-1]+t2[-2]=="00":
    h = int(float(t2)-float(t1))//1
    if int(t1[-2]+t1[-1])==0 : m=0
    else : m = 60-int(t1[-2]+t1[-1])
else : 
    h = int(float(t2)-float(t1))//1
    m = int(t2[-2]+t2[-1])-int(t1[-2]+t1[-1])
print(f"You parked in for {h} hour(s) and {m} minute(s).")

if h==0 and m<=30 : 
    print("You will not be charged !!!.")
    print("You will pay 0 baht.")
elif h==2 and m==0 :
    print("You will be charged for the first 2 hour(s).")
    print("You will pay 40 baht.")
elif h<2 and m>0 :
    print(f"You will be charged for the {h+1} hour(s).")
    print("You will pay 40 baht.")
elif 6>h>2 and m>0 :
    print(f"You will be charged for {h+1} hour(s).")
    print(f"You will pay {(h+1-2)*100+40} baht.")
elif h>=6 and m==0 :
    print(f"You will be charged for {h} hour(s).")
    print("You will pay 500 baht.")
elif h>=6 and m>0 :
    print("You will be charged for the maximum rate.")
    print("You will pay 2000 baht.")