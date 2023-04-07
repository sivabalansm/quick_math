import os

def manage(path):
    # string parsing the path
    path = r"{}".format(path)

    # check if path exisits and create if not
    if os.path.exists(path):
        content = os.listdir(path)

        # get into path for file creation
        os.chdir(path)
        
        if content:
            # store files with .xlsx extension and that contain the path in them in a list
            xlsx_files = [xlsx_file for xlsx_file in content if path in xlsx_file and ".xlsx" in xlsx_file]
            xlsx_files.sort()
            
            # from the last filename, remove .xlsx and store the last file number in variable
            last_number = xlsx_files[-1].rstrip(".xlsx")[-1]

            # return the last number of the file and if not then return 0
            if last_number.isdigit():
                return int(last_number)
            else:
                return 0

            
        # return 0 since nothing in folder
        else:
            return 0

        

    else:
        os.mkdir(path)

        # rerun funtion after creating path
        manage(path)

        
