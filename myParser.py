import pandas as pd
import os

def readData(path, file_group):
    sheet = pd.read_excel(path, sheet_name='Informatik')

    group = []
    for val in sheet[file_group]:
        if (type(val) == str):
            group.append(val)
        else:
            break
    
    return group

def trimData(data):
    
    for entry in data:
        print(entry)

def main():
    #path = str(input("Enter spreadsheet path: "))
    path = r"X:\Programming\Python\Excel_Parser\Data.xlsx"
    group = "Gruppe 01"
    data = readData(path, group)
    trimData(data)


if __name__ == "__main__":
    main()    