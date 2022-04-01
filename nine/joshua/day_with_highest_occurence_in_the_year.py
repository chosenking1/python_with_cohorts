# Author: Joshua
# Title : Checking for the day that appeared most in the year.
daysOfTheWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
year = int(input("What Year Do you Want to Check For"))
highest_day = "Monday"
i = 1
count = 0


def year_is_leap_year(year_checked):
    if year_checked % 4 == 0 and year_checked % 100 != 0:
        print('it is a leap year')

    elif year_checked % 400 == 0:
        print('it is a leap year')


while i <= year:
    highest_day = daysOfTheWeek[count]
    if year_is_leap_year(year):
        highest_day = daysOfTheWeek[count] + "and" + daysOfTheWeek[count + 1]
