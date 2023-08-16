import pandas as pd
import os

def readData(sheet, __file_group__):
    try:
        group = []
        for val in sheet[1:]:
            if isinstance(val, str):
                group.append(val)
                print(val)
            else:
                break

        return group
    except Exception as e:
        print("Error reading data:", e)

        return []

def trimData(data):
    A = []
    for entry in data[1:]:
        A.append(entry.split())

    return A

def main():
    try:
        # path = str(input("Enter spreadsheet path: "))
        path = os.path.join(os.curdir, "Data.xlsx")
        sheet = pd.read_excel(path, sheet_name="Informatik")

        groupData = []
        group = "Gruppe 01"
        data = readData(sheet, group)
        groupData.append(trimData(data))

        #print(groupData)

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
