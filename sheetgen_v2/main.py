#!/bin/python3
from sheetgen import gen
from time import sleep
import pathmanager

while 1:
    try:
        times = int(input("Paper quantity: "))
        numbers = int(input("Numbers per equation: "))
        digits = int(input("Digits for the numbers: "))
        break
    except Exception as error:
        print("Enter integer values only")
        sleep(2)

foldername = f'{digits}_digits_{numbers}_numbers'
last_num = pathmanager.manage(foldername)

for time in range(times):
    gen(f'{digits}_digits_{numbers}_numbers_number_{last_num + time + 1}.xlsx', digits, numbers)

