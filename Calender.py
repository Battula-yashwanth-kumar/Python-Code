import calendar
from calendar import HTMLCalendar

# 1. Print the calendar for a specific month (August 2024)
print("### Calendar for August 2024 ###")
print(calendar.month(2024, 8))

# 2. Print the calendar for the entire year (2024)
print("\n### Calendar for the year 2024 ###")
print(calendar.calendar(2024))

# 3. Get the weekday for a specific date (August 11, 2024)
weekday = calendar.weekday(2024, 8, 11)
print(f"\n### Weekday for August 11, 2024 ###\nWeekday: {weekday} (0=Monday, 6=Sunday)")

# 4. Check if a specific year is a leap year (2024)
is_leap = calendar.isleap(2024)
print(f"\n### Is 2024 a Leap Year? ###\n{is_leap}")

# 5. Count the number of leap years between 2000 and 2024
leap_years = calendar.leapdays(2000, 2024)
print(f"\n### Number of Leap Years between 2000 and 2024 ###\n{leap_years}")

# 6. Create and print an HTML calendar for August 2024
html_cal = HTMLCalendar().formatmonth(2024, 8)
print("\n### HTML Calendar for August 2024 ###")
print(html_cal)

# 7. Get the first weekday and number of days in August 2024
first_weekday, days_in_month = calendar.monthrange(2024, 8)
print(f"\n### First Weekday and Number of Days in August 2024 ###\nFirst Weekday: {first_weekday} (0=Monday, 6=Sunday), Days: {days_in_month}")

# 8. Set the first day of the week to Sunday
calendar.setfirstweekday(calendar.SUNDAY)
print("\n### Set the first day of the week to Sunday ###")
print(calendar.month(2024, 8))

# 9. Get a matrix representing a month’s calendar (August 2024)
month_matrix = calendar.monthcalendar(2024, 8)
print("\n### Matrix representation of August 2024 ###")
for week in month_matrix:
    print(week)
