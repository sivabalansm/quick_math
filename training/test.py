while 1:
        #asking number of digits and amount of numbers
        try:
            ask_digit = int(input("Number of digits for generator>"))
            ask_numbers = int(input("Amount of numbers for generator>")) 
            #only breaks if the two or numbers
            if type(ask_digit) == type(int()): and type(ask_numbers) == type(int()):
                break
            else:
                print("Please enter numbers" )
        except ValueError:
            print("Please enter numbers")

        
