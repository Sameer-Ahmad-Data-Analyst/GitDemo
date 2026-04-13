
"""Task 1: Read a File and Handle Errors
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
"""

#Solution: -

"""
First create a file and type below lines in the file: - 
Reading file content: 
Line 1: This is a sample text file. 
Line 2: It contains many lines. 
"""
mo = open("sample_text.txt", "xt")
mo.write("Reading file content: \n")
mo.write("Line 1: This is a sample text file. ")
mo.write("\n Line 2: It contains many lines. ")

#Then remove the upper code because the file is created and use the below codes.

#Now open and read it as a text file named sample.txt
file_name = "sample_text.txt"
try:
   # 1. Opens and reads the file using a context manager
   with open(file_name, "r") as file:
       # 2. Iterates through the file and prints line by line
       for line in file:
           # .strip() removes the newline character at the end of each line
           print(line.strip())
# 3. Handles the error if the file does not exist
except FileNotFoundError:
   print(f"Error: The file '{file_name}' was not found.")


"""Task 2: Write and Append Data to a File
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
"""

#1. taking user input and writing it to output.txt

user_input = input("Enter text to write to the file: ")
print("Data successfully written to output.txt.")
with open("output.txt", "w") as file:
    file.write(user_input + "\n")

print("\n Enter additional text to append: Learning file handling in Python.")

#2. Appending additional data to the same file.
print(" Data successfully appended.")
extra_data = "Learning file handling in Python."
with open("output.txt", "a") as file:
    file.write(extra_data + "\n")


#3. Reading and displaying it to the final content.

with open("output.txt", "r") as file:
    content = file.read()
    print("\nFinal content of output.txt ")
    print(content)
