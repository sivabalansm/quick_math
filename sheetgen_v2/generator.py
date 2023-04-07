#!/bin/python3
from random import randint

class csum:
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
            minimum = int('1' + ('0' * (digits-1)))

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

# create multiplication 
class cmult:
    # digits multiplicand and muliplicator
    def __init__(self, digit_cand=int(), digit_cator=int()):
        self.digit_cand = digit_cand
        self.digit_cator = digit_cator

    # alternative set
    def set_digit_cand(self, digits):
        self.digit_cand = digits

    def set_digit_cator(self, digits):
        self.digit_cator = digits


    def gen(self):
        if self.digit_cator > 0 and self.digit_cand > 0:
            cand = randint(int("1" + ("0" * (self.digit_cand-1))), int("9" * self.digit_cand))
            cator = randint(int("1" + ("0" * (self.digit_cator-1))), int("9" * self.digit_cator))
            total = cand * cator
            return ((cand, cator), total)


class cdiv:
    # digits divisor and quotient
    def __init__(self, digit_divi=int(), digit_quot=int()):
        self.digit_divi = digit_divi
        self.digit_quot = digit_quot

    # alternative set
    def set_digit_divi(self, digits):
        self.digit_divi = digits

    def set_digit_quot(self, digits):
        self.digit_quot = digits

    def gen(self):
        if self.digit_divi > 0 and self.digit_quot > 0:
            divi = randint(int("1" + ("0" * (self.digit_divi-1))), int("9" * self.digit_divi))
            quot = randint(int("1" + ("0" * (self.digit_quot-1))), int("9" * self.digit_quot))
            # finding dividend using divisor * quotient
            divid = divi * quot
            return ((divid, divi), quot)
            


if __name__ == "__main__":
#    test = csum()
#    test.set_digits(3)
#    test.set_numbers(4)
#    for _ in range(100): print(test.gen())
    test2 = cmult()
    test2.set_digit_cand(3)
    test2.set_digit_cator(2)
    test3 = cdiv(2, 2)

    for _ in range(100): print(test3.gen())



            






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

