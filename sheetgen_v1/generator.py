#!/bin/python3
from random import randint

class equations:
    # set default to int if no quantity is set
    def __init__(self, digits=int(), numbers=int()):
        self.digits = digits
        self.numbers = numbers

    # set digits and numbers for readability purposes in oop programming
    def set_digits(self, digits):
        self.digits = digits

    def set_numbers(self, numbers):
        self.numbers = numbers

    def gen(self):

        # start if more than 0 digits and number (default int -> 0)
        if self.digits > 0 and self.numbers > 0:
            digits = self.digits
            numbers = self.numbers

            # maximum and minimum
            maximum = int('9' * digits)

            # more than 1 digit minimum and 1 digit minimum
            if digits > 1:
                minimum = int('1' + ('0' * (digits-1)))
            else:
                minimum = int('1')

            # first positive number
            numlist = [randint(minimum, maximum)]

            while len(numlist) < numbers:
                total = sum(numlist)

                # pick negative or positive (positive if total is 0)
                if total == 0:
                    choice = 1
                else:
                    choice = randint(0,1)

                # append positive or negative number
                if choice == 1:
                    numlist.append(randint(minimum, maximum))

                else:
                    numlist.append(-randint(1, total))

            return (numlist, sum(numlist))

if __name__ == "__main__":
    test = equations()
    test.set_digits(3)
    test.set_numbers(4)
    for _ in range(100): print(test.gen())


            






"""
features:
equation with step by step summing
multiplication
formatter functio to have all nums alligned 
division
save equation for difficulty practice
csv mode
default profiles
"""

