# Give user command options
cmd = input("(h)armonic, (m)ultiplication or (q)uit: ")

while cmd != "q":

    if cmd == "h":
        # Run ´harmonic series´ program

        n = int(input("Series length: "))

        # Create variable 'sum' that can be used to add the numbers of the series. Set to default value of 0.
        sum = 0

        # Use for-loop to print each number of the series and add its value to the sum.
        # Since the harmonic series consists of numbers with increasing divisors (1/1, 1/2, 1/3, etc)..
        # ..make sure to start the range at 1. End it at n + 1, so n is included.
        for num in range(1, n+1):
            sum += 1 / num
            print(str(round(1 / num, 4)))
        print(str(round(sum, 4)))
        cmd = input("(h)armonic, (m)ultiplication or (q)uit: ")

   
   
    # if cmd == "m":


    # cmd = input("(h)armonic, (m)ultiplication or (q)uit: ")