total = int(input("Enter the total amount: "))

if total<100:
    total = total + 20
elif (total>=100 and total<=500):
    total = total + 50
else:
    total = total + 100

print("Total =", total)
