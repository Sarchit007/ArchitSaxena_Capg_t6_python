units = int(input("Enter units consumed: "))

bill = 0

if units <= 100:
    bill = units * 5

elif units <= 300:
    bill = (100 * 5) + (units - 100) * 7

else:
    bill = (100 * 5) + (200 * 7) + (units - 300) * 10

print("Total Bill Amount:", bill)