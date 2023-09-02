location = "1234567890"
name = input("Name: ")
sex = input("SEX (M/F): ")
n = int(input("NUMBER (100-999): "))
gpa = float(input("GPA: "))
print(location*4)
print("%-15s"%"NAME"+"%-9s"%"SEX"+"%-13s"%"NUMBER"+"GPA")
print("%-16s"%name+"%-11s"%sex+"%-8d"%n+"%.3f"%gpa)