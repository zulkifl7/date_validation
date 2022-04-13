'''
Write a Python program to check whether a given date is valid date or not and to out put the
following.
• If the date is valid then the message “Date is Valid” otherwise the message “Date is
Invalid”.
• If the date is a valid date, then the next date.

Hint:

Follow the following steps. (NOTE: You are not allowed to use any Python built-in functions.)
• Get the inputs Year, Month, and Date separately.
• Use selection statements, i.e., if-else statements to check if the Date, Month, and the Year are
valid.
• if the date is a valid date, then print the next date (Increment the date).
Sample Test Cases:
            Enter the Year | Enter the Month | Enter the Date | Expected Result | Next Date
Test Case 1   2020                02              30            Date is Invalid     -
Test Case 2   2020                02              29            Date is Valid    01-03-2021
Test Case 3   2021                09              31            Date is Invalid     -
Test Case 4   2021                13              01            Date is Invalid     -
Test Case 5   2021                08              31            Date is Valid    01-09-2021 
'''

year = int(input("Year: "))
month = int(input("Month: "))
day = int(input("Day: "))

day28 = [2]
day30 = [4, 6, 9, 11]
day31 = [1, 3, 5, 7, 8, 10, 12]

feb = 28
if (year % 4 == 0):
    feb = 29

if (month in day28 and 1 <= day <= feb):
    if (day == feb):
        day = 1
        month += 1
    else:
        day += 1
    print("Date is valid. \nNext date: %d-%d-%d" % (day, month, year))
elif (month in day30 and 1 <= day <= 30):
    if (day == 30):
        day = 1
        month += 1
    else:
        day += 1
    print("Date is valid. \nNext date: %d-%d-%d" % (day, month, year))
elif (month in day31 and 1 <= day <= 31):
    if (day == 31):
        day = 1
        month += 1
        if (month > 12):
            year += 1
            month = 1
            day = 1
    else:
        day += 1
    print("Date is valid. \nNext date: %d-%d-%d" % (day, month, year))
else:
    print("Date is invalid")
