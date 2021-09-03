# Prompt user to input length of sequence
n = int(input("Enter the length of the sequence: ")) # Do not change this line

# The first 3 numbers are 1, 2, 3
# The following numbers can be calculated by summing the former 3 numbers.

# Set default values for the 1st, 2nd, 3rd and new number. 
# Also set a counter so the while loop will run n times and print n numbers of the sequence.
counter = 0
first_num = 0
second_num = 1
third_num = 2
new_num = 3

while counter < n:
    # Print the first 3 numbers 
    while counter < 3:
        print(1)
        counter += 1
        print(2)
        counter += 1
        print(3)
        counter += 1
    # Calculate every next number by adding the former 3 numbers
    first_num = second_num
    second_num = third_num
    third_num = new_num
    new_num = first_num + second_num + third_num
    # Print the number and add 1 to the counter
    print(new_num)
    counter += 1