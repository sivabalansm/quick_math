#! /bin/python
import xlsxwriter
from generator import equations

def gen(filename, digits, numbers):

    # basis for filenameing with this program

    # object to generate the equations from our other script
    equation_creator = equations(digits, numbers)

    # creating file and sheet of xlsx file
    file = xlsxwriter.Workbook(filename)
    question_sheet = file.add_worksheet()
    answer_sheet = file.add_worksheet()

    # cell formatting
    fontsize = 18
    border_style = 2
    color = '#000000' # black color
    top_cell_format = file.add_format({'font_size': fontsize, 'border_color': color, 'top': border_style, 'left': border_style, 'right': border_style})
    middles_cell_format = file.add_format({'font_size': fontsize, 'border_color': color, 'left': border_style, 'right': border_style})
    bottom_cell_format = file.add_format({'font_size': fontsize, 'border_color': color, 'bottom': border_style, 'left': border_style, 'right': border_style})
    answer_cell_format = file.add_format({'font_size': fontsize, 'border_color': color, 'border' : border_style})
    generic_cell_format = file.add_format({'font_size': fontsize})

    # inserting all the equations
    for col in range(20):

        # sums list and answers 
        sum_list, answer = equation_creator.gen()

        # equations numbered 1 to 20
        if col <= 9:
            question_sheet.write(0, col, col+1, answer_cell_format)
            answer_sheet.write(0, col, col+1, answer_cell_format)
        else:
            question_sheet.write(numbers+2, col-10, col+1, answer_cell_format)
            answer_sheet.write(2, col-10, col+1, answer_cell_format)
        for row in range(numbers):
            # set current format for cell according to row
            if row == 0:
                current_cell_format = top_cell_format
            elif row == (numbers-1):
                current_cell_format = bottom_cell_format
            else:
                current_cell_format = middles_cell_format

            # write numbers according cell
            if col > 9:
                question_sheet.write(row+numbers+3, col-10, sum_list[row], current_cell_format)
                answer_sheet.write(3, col-10, answer, generic_cell_format)
                #print(row, col, sum_list[row])
            else:
                question_sheet.write(row+1, col, sum_list[row], current_cell_format)
                answer_sheet.write(1, col, answer, generic_cell_format)
                #print(row, col, sum_list[row])

            # write area for answer
            if row == (numbers-1) and col <= 9:
                question_sheet.write(row+2, col, "", answer_cell_format)
                #print(row+1, col, "space")

            elif row == (numbers-1) and col > 9:
                question_sheet.write(row+numbers+4, col-10, "", answer_cell_format)
                #print(row+1, col-10, "space")

    # Defacto close like all files used in python
    file.close()

if __name__ == "__main__":
    gen(3, 5, 1)

