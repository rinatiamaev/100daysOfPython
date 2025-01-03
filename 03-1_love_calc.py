print("Hello and welcome to the love calculator!")
name1 = input("Input your name: ")
name2 = input("Input your partner`s name: ")
name1 = name1.lower()
name2 = name2.lower()
totalname = name1 + name2
count1 = 0
count2 = 0
searchletter1 = ['t', 'r', 'u', 'e']
searchletter2 = ['l', 'o', 'v', 'e']
for char in totalname:
    if char in searchletter1:
        count1 += 1
for char in totalname:
    if char in searchletter2:
        count2 += 1
count = str(count1) + str(count2)
count = int(count)
if count > 90 or count < 10:
    print("You are like Biwis and Badhead")
elif count > 40 and count < 50:
    print("Yours love is great!")
else:
    print(f"Your love score is {count}")