#!/bin/python3
import random
def minus():
    numlist = list()
    print()
    for nums in range(16):
        randint = random.randint(1,4)
        numlist.append("-"+str(randint))
        print(str("-")+str(randint), end = " | ")    
    conditional_answer = input()
    if conditional_answer.lower() == 'answer':
        for reursion in range(16):
            print("   | ",end = "")
        print()
        for nums in numlist:
            print(" "+str(5+int(nums)),end = " | ")
        print()
        
def add():
    numlist = list()
    print()
    for nums in range(16):
        randint = random.randint(1,4)
        numlist.append(randint)
        print(str(randint), end = "  | ")

    conditional_answer = input()
    if conditional_answer.lower() == 'answer':
        for reursion in range(16):
            print("   | ",end = "")
        print()
        for nums in numlist:
            print(str(4+int(nums)),end = "  | ")
        print()
if __name__ == "__main__":
    try:
        while True:
            minus()
            add()
    except KeyboardInterrupt:
        print()
        exit()
