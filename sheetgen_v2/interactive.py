#!/bin/python3

import generator as gen

def main():
    # function to call num index
    functions = (gen.csum, gen.cmult, gen.cdiv)

    # input template with num index
    inputs = (("sum", "digits", "numbers"), ("multiplication", "cand digits", "cator digits"), ("division", "quotient digits", "dividend digits"))

    print("Enter options w/ space seperated values:\n1) Sums\n2) Multiplication\n3) Division")
    nums = input("#> ")
    values = nums.split(" ")

    # validity of inputs
    if len(values) > 0 and nums.replace(" ", "").isdigit() and len(values) <= 3 and all(int(num) in range(1, 4) for num in values):
        nums = list(map(int, values))
        # programming indexes fix
        nums = set([num-1 for num in nums])


        # demanding answers with inputs template and using nums as index
        # checkinf if all inputs for answers are valid
        check = [False]
        while not all(check):
            check = list()
            answers = [(keys, input("For the " + inputs[keys][0] + " what are the " + inputs[keys][1] + " and the " + inputs[keys][2] + " respectively")) for keys in nums]
            for answer in answers:
                answer = answer[1]
                if answer.replace(" ", "").isdigit() and all(int(num) > 0 for num in answer.split(" ")) and len(answer.split(" ")) == 2:
                    check.append(True)
                else:
                    print("invalid input")
                    check.append(False)
                    break
        
        answers = [(keys, tuple(map(int, answer.split(" ")))) for keys,answer in answers]
        while 1:
            for keys,answer in answers:
                print(functions[keys](answer[0], answer[1]).gen())
                input()
            
            


    else:
        print("Underterminable values detected")
        main()
        




if __name__ == "__main__":
    main()

