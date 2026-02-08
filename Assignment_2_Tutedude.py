#Task 1: - Check if a Number is Even or Odd.

a = float(input ("Enter a number: "))
if a % 2 == 0:
    print("even number")
else:
    print("odd number")

#Task 2: - Sum of Integers from 1 to 50 Using a Loop.

total_sum = 0
for i in range(1,51):
    total_sum += i
print("The sum of numbers from 1 to 50 is: ",total_sum)
