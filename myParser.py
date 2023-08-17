import pandas as pd
import os
import re

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
    for entry in data:
        for group in entry:
            val = re.split('-| ', group)
            A.append(val)

    return A

def packData(data, subjects):
    sub_day = []
    group = []
    final = []
    i = 0
    for entry in data:
        sub_day.append(subjects[i])
        sub_day.append(entry)
        group.append(sub_day)
        sub_day = []
        i += 1
        if i == len(subjects):
            final.append(group)
            group = []
            i = 0

    return final

def addTimeslot(data):
    for group in data:
        if len(group) != 4 or group[-1][0] == '[':
            group.append("(z)")

def main():
    try:
        # path = str(input("Enter spreadsheet path: "))
        path = os.path.join(os.curdir, "Data.xlsx")
        sheet = pd.read_excel(path, sheet_name = "Informatik")

        trimmedData = []

        # reads the data group by group
        # includes the subjects at the end of the list
        data = readData(sheet)

        # copy the subject list from the data list
        subjects = data[-1]

        # cut the subjects out of the data list
        data.remove(data[-1])

        if data:
            # trims the data to single strings
            # chunk: day - from - to - professor/timeslot
            trimmedData = trimData(data)

            # empty data list
            data = []

            # adds the timeslot if missing at the end
            # z => every week
            addTimeslot(trimmedData)

            # puts subject and trimmedData into one list in the bigger data list
            # produces a list of lists which contain the single days with their given subject
            data = packData(trimmedData, subjects)
        else:
            print("Error while reading")
            return -1

        for group in data:
            for entry in group:
                print(entry)
            print("\n")


    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
