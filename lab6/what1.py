s = input("Enter a String: ")
print("You entered",'"'+s+'"')
print("You enterd",len(s),"characters.")
print("The first character is","'"+(s[0])+"'.")
print("The last character is","'"+(s[-1])+"'.")
print("The first five-character is","'"+(s[0:5])+"'.")
print('"'+s+'"',"is reversed to",'"'+(s[-1::-1])+'".')