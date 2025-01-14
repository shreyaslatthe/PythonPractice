#Break statement
s = "I love python"
for i in s:
    print(i)
    if (i == 'v'):
        break
print("The end of statement")

l1 = ["java", "sql", "python", "asp.net"]
for index in range(len(l1)):
    print(l1[index])
    if (l1[index] == "sql"):
        continue
print("The end of statement")


