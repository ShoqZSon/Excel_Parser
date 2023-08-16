import pandas as pd
import os

def readData(sheet):
    try:
        subjects = []
        semester_group = []
        num_columns = len(sheet.columns)
        for col_index in range(num_columns):
            group = []
            column_data = sheet.iloc[:, col_index]
            for val in column_data[1:]:
                if isinstance(val, str):
                    if col_index == 0:
                        subjects.append(val)
                    else:
                        group.append(val)
                else:
                    if group:
                        semester_group.append(group)

                    break

        semester_group.append(subjects)

        return semester_group

    except Exception as e:
        print("Error reading data:", e)

        return []


def trimData(data):
    A = []
    for entry in data[1:]:
        for group in entry[1:]:
            A.append(group.split())

    return A

def packData(data, subjects):
    sub_day = []
    group = []
    final = []
    i = 0
    for entry in data:
        for val in entry:
            if i != len(subjects):
                sub_day.append(subjects[i])
                sub_day.append(val)
                group.append(sub_day)
                sub_day = []
                i += 1
            else:
                final.append(group)
                group = []
                i = 0

    for entry in final:
        for val in entry:
            print(val)


def main():
    try:
        # path = str(input("Enter spreadsheet path: "))
        path = os.path.join(os.curdir, "Data.xlsx")
        sheet = pd.read_excel(path, sheet_name = "Informatik")

        trimmedData = []
        data = readData(sheet)
        subjects = data[-1]
        data.remove(data[-1])

        if data:
            packData(data, subjects)
            #trimmedData.append(trimData(data))
        else:
            print("Error while reading")
            return -1


        #print(trimmedData)

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
