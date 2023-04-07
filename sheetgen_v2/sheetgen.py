#! /bin/python
import xlsxwriter

"""
matrix format 3x2, 5x2
3x2
|_|_|_|
|_|_|_|
in main, have defaults or option to create default preset in json or smth
single cell can have different quantity of numbers (incorperate multiplication and sums in one sheet)
integrate comments at top of page
"""

def sheetgen(filename, g_width, g_height, total_nums, fontsize=18, comment=None):
    # expect tuple of numbers and answers
    if g_width * g_height != len(total_nums):
        raise Exception("Excel grid area must be equal to total equations")
        exit(1)

    # creating file and sheet of xlsx file
    file = xlsxwriter.Workbook(filename)
    equation_sheet = file.add_worksheet()
    answer_sheet = file.add_worksheet()

    # cell formatting
    border_style = 2
    color = '#000000' # black color
    top_cell_format = file.add_format({'font_size': fontsize, 'border_color': color, 'top': border_style, 'left': border_style, 'right': border_style})
    middles_cell_format = file.add_format({'font_size': fontsize, 'border_color': color, 'left': border_style, 'right': border_style})
    bottom_cell_format = file.add_format({'font_size': fontsize, 'border_color': color, 'bottom': border_style, 'left': border_style, 'right': border_style})
    full_cell_format = file.add_format({'font_size': fontsize, 'border_color': color, 'border' : border_style})
    generic_cell_format = file.add_format({'font_size': fontsize})

    # add a comment at the top of the page
    if comment:
        equation_sheet.write(0, 0, comment, generic_cell_format)
        answer_sheet.write(0, 0, comment, generic_cell_format)
        row_padding = 1

    for row in range(g_height):
        for col in range(g_width):
            equation_sheet.write(row + row_padding, col, (col+1) * (row+1), full_cell_format)
            answer_sheet.write(row * 2, col, (col+1) * (row+1), full_cell_format)

    # inserting all the equations
    for col in range(20):

        # sums list and answers 
        sum_list, answer = equation_creator.gen()

        # equations numbered 1 to 20
        if col <= 9:
            equation_sheet.write(0, col, col+1, full_cell_format)
            answer_sheet.write(0, col, col+1, full_cell_format)
        else:
            equation_sheet.write(numbers+2, col-10, col+1, full_cell_format)
            answer_sheet.write(2, col-10, col+1, full_cell_format)
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
                equation_sheet.write(row+numbers+3, col-10, sum_list[row], current_cell_format)
                answer_sheet.write(3, col-10, answer, generic_cell_format)
                #print(row, col, sum_list[row])
            else:
                equation_sheet.write(row+1, col, sum_list[row], current_cell_format)
                answer_sheet.write(1, col, answer, generic_cell_format)
                #print(row, col, sum_list[row])

            # write area for answer
            if row == (numbers-1) and col <= 9:
                equation_sheet.write(row+2, col, "", full_cell_format)
                #print(row+1, col, "space")

            elif row == (numbers-1) and col > 9:
                equation_sheet.write(row+numbers+4, col-10, "", full_cell_format)
                #print(row+1, col-10, "space")

    # Defacto close like all files used in python
    file.close()

if __name__ == "__main__":
    gen(3, 5, 1)

