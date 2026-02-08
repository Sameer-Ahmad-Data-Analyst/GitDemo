
#Calculate Factorial Using a Function .

def fact(num):
   factorial = 1
   while num > 1:
       factorial *= num
       num -= 1
   return factorial


n = int(input("Enter the number: - "))
print(f" Factorial of {n} is: {fact(n)}")


import math
a = float(input("Enter the number: - "))
square_root = math.sqrt(a)
natural_log = math.log(a)
sine_value = math.sin(a)

print(f"--- Results for {a} ---")
print(f"Square root: {square_root}")
print(f"Natural Logarithm (ln): {natural_log}")
print(f"Sine (in radians):    {sine_value}")
