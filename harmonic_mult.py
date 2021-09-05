# Give user command options
cmd = input("(h)armonic, (m)ultiplication or (q)uit: ")

while cmd != "q":

    if cmd == "h":
        # Run ´harmonic series´ program, which prints nrs of the harmonic series and their sum.

        n = int(input("Series length: "))

        # Create variable 'sum' that can be used to add the numbers of the series. Set to default value of 0.
        sum = 0

        # Use for-loop to print each number of the series and add its value to the sum.
        # Since harmonic series consists of nrs with increasing divisors (1/1, 1/2, 1/3, etc)..
        # ..make sure to start the range at 1. End it at n + 1, so n is included.
        for num in range(1, n+1):
            sum += 1 / num
            print(str(round(1 / num, 4)))
        print("Sum of series: " + str(round(sum, 4)))
        cmd = input("(h)armonic, (m)ultiplication or (q)uit: ")

    elif cmd == "m":
        # Run multiplication program, which performs the Ancient Egygptian method for multiplication.

        # Prompt user for 2 integers
        first_num = int(input("First integer: "))
        second_num = int(input("Second integer: "))

        # Set default value for product
        product = 0

        while second_num > 0:
            print(str(first_num) + " " + str(second_num))
            # add value of the first number to product when second number is odd.
            if second_num % 2 == 1:
                product += first_num
            first_num = first_num * 2
            second_num = second_num // 2
            
        print("Product: " + str(product))
        cmd = input("(h)armonic, (m)ultiplication or (q)uit: ")

    elif cmd != "h" or "m" or "q":
        print("Illegal choice!")
        cmd = input("(h)armonic, (m)ultiplication or (q)uit: ")