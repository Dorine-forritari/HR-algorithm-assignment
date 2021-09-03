# Prompt user to input length of sequence
n = int(input("Enter the length of the sequence: ")) # Do not change this line

# The first 3 numbers are 1, 2, 3
# The following numbers can be calculated by summing the former 3 numbers.

# Set default values for the 1st, 2nd, 3rd and new number. 

first_num = 1
second_num = 2
third_num = 3
new_num = 0

if n >= 1:
    print(1)
if n >= 2:
    print(2)
if n >= 3:
    print(3)
if n >= 4:
   for num in range(n-3):
        new_num = first_num + second_num + third_num
        print(new_num)
        first_num = second_num
        second_num = third_num
        third_num = new_num
