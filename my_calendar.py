
import calendar
import argparse
import shutil
from colorama import Fore, Back, Style, init
from datetime import datetime

holidays = {
    (1, 1): "New Year's Day",
    (7, 4): "US Independence Day",
    (12, 25): "Christmas Day"
}

def get_month_str(year, month):
    cal = calendar.Calendar()
    month_cal = cal.monthdays2calendar(year, month)
    month_str = f"{calendar.month_name[month].center(20)}\n"

    for week in month_cal:
        if week == month_cal[0]:
            month_str += "Mo Tu We Th Fr Sa Su\n"

        for day, weekday in week:
            if day == 0:
                month_str += weekday < 6 and "   " or "  "
            elif (month, day) in holidays:
                month_str += f"{Fore.GREEN}{day:2d}{Style.RESET_ALL} "
            elif weekday == 5 or weekday == 6:
                month_str += f"{Fore.RED}{day:2d}{Style.RESET_ALL}"
                month_str += weekday == 5 and " " or ""
            else:
                month_str += f"{day:2d} "
        month_str += "\n"

    if len(month_cal) < 6:
        month_str += "                    \n"

    return month_str

def print_calendar(year):
    months = [get_month_str(year, month) for month in range(1, 13)]

    print(f"{year}".center(64), end="\n")

    for i in range(0, 12, 3):
        month_block = [months[i], months[i+1], months[i+2]]
        month_lines = [month.split('\n') for month in month_block]

        for lines in zip(*month_lines):
            print("  ".join(lines))

# Get input year from user
parser = argparse.ArgumentParser(description="Print a calendar for a given year.")
parser.add_argument("year", nargs="?", type=int, default=datetime.now().year, help="Year for the calendar (default: current year)")
args = parser.parse_args()

# Print the calendar
print_calendar(args.year)
