#!/bin/python3
from random import randint

class generate_sum:
    def __init__(self, digits):
        #get number of digits ex: 3 for 3 digit numbers (ex: 368)
        self.digits = digits

    #generate minimum number with number of digits
    def minimum(self):
        minimum = str()
        #make the minimum a multiple of 10 so you get minimum
        for placement in range(self.digits):
            #if the first number in the range is one (so first loop)
            if placement == 0:
                #set the first digit of the minimum to 1
                minimum += '1'
            else:
                #and then set the rest to 0 so you get a multiple of 10
                minimum += '0'
        return int(minimum)

    def maximum(self):
        maximum = str()
        #set the maximum number with the number of digits
        for _ in range(self.digits):
            maximum += '9'
        return int(maximum)

    def gen(self, minimum, maximum, numbers):
        total_sum = 0
        plus_or_minus = int()
        numbers_output = []
        #making list of numbers with the amount of numbers provided
        for number_ in range(numbers):
            #setting the first number to postive so we don't start with a negative number
            if number_ == 0:
                number = randint(minimum, maximum)
            #if the total_sum is lower than the minimum (so that that something like this doesn't happen ranint(100, 24))
            elif total_sum < minimum:
                number = randint(minimum, maximum)
            else:
                #adding negative numbers to the mix
                plus_or_minus = randint(0,1)
                #if the number is one, then the number will be positive
                if plus_or_minus == 1:
                    number = randint(minimum, maximum)
                #if not, then it will be negative
                else:
                    number = randint(minimum, total_sum)
                    number = -number
            #adding the number to the std.output and summing it 
            numbers_output.append(number)
            total_sum += number
        #returning both in a single list
        return [numbers_output, total_sum]        
        
def main():
    try:
        while 1:
            #asking number of digits and amount of numbers
            try:
                ask_digit = int(input("Number of digits for generator>"))
                ask_numbers = int(input("Amount of numbers for generator>")) 
                #only breaks if the two or numbers
                if type(ask_digit) == type(int()) and type(ask_numbers) == type(int()):
                    break
                else:
                    print("Please enter numbers" )
            except ValueError:
                print("Please enter numbers")
        #provide the digits to the generator
        generator = generate_sum(ask_digit)
        #generate numbers infnetly
        count = 0
        while True:
            try:
                #generate a list of numbers with the amount of numbers provided in the input
                new_sum = generator.gen(generator.minimum(), generator.maximum(), ask_numbers)
                count += 1
                #unpacking the returned list into seperate variables
                output_numbers = new_sum[0]
                answer = new_sum[1]
                #printing the output and waiting for an input before giving the answer
                input('--sum #{}--'.format(count))
                for number in output_numbers:
                    print(number)
                input('--answer--')
                print(answer)
            except KeyboardInterrupt:
                break
#                print();main()
    except KeyboardInterrupt:
        print()
#        main()
if __name__ == "__main__":
    main()
