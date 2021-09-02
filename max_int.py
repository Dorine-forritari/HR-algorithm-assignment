# Ask user to input numbers until a negative value is entered.

num_int = int(input("Input a number: "))    # Do not change this line

# Find the maximum positive integer:
# Compare input with last input and save if number is higher.
max_int = 0

# While input is positive value
while num_int > 0:
    # If the new number is higher than the highest number so far...
    if num_int > max_int:
        #... save the new number in max_int
        max_int = num_int
    # Ask for new number
    num_int = int(input("Input a number: "))

print("The maximum is", max_int)    # Do not change this line"""