w = input("Please enter a word: ")
v = "aeiouAEIOU"
count1,count2 = 0,0
vowel,con = "",""
for x in w :
    for i in v :
        if x == i :
            vowel = vowel+i
            count1 = count1+1
    if x not in v :
        con = con+x
        count2 = count2+1
print(f"Total vowel found = {count1}")
print(vowel,end="")
print(f"\nTotal consonant found = {count2}")
print(con,end="")