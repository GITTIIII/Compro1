n = "1234567890"
name = "Somchai Jaidee"
age = 21
weight = 56.5
sex = "M"
print("Using space determination with %d, %f and %s to print out ...")
print(n*4)
print("%-20s"%"NAME"+
    "%-5s"%"AGE"+
    "%-12s"%"WEIGHT"+
    "SEX")
print("%-20s"%name+
    "%-5d"%age+
    "%-13.4f"%weight+
    sex)