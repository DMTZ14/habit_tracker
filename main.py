"""
from stats import (
    get_minutes_by_habit,
    get_minutes_by_category,
    get_top_habits,
    get_global_stats,
)
import datetime
"""
from multiprocessing.connection import deliver_challenge

from models import Session, HabitTracker
from validators import is_valid_date, is_valid_category
from time import asctime,localtime


def main():
    tracker = HabitTracker()
    while True:
        choice= menu()
        print()
        if choice =="1":
            handle_add_session(tracker)
        elif choice =="6":
            print("Goobye!\n")
            break
        else:
            print("Feature not yet implemented\n")
def menu():
    print(
        "=== HabitForge: Habit Tracker ===\n"
        "1. Add new session\n"
        "2. View today's summary\n"
        "3. View summary by date range\n"
        "4. View global statistics\n"
        "5. Export summary to file\n"
        "6. Exit\n"
        "Choose an option: ",
        end="",
    )
    return input().strip()

def todaysdate():
    texto = asctime(localtime())
    time = texto.split(" ")
    months = {
        "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
        "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
        "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
    }
    day = time[2]
    month = months[time[1]]
    year = time[4]
    date = f"{year}-{month}-{day}"
    return date


def handle_add_session(tracker: HabitTracker):
    # Date
    while True:
        today= input("Is it today?\n"
                     "1. Yes\n"
                     "2. No\n"
                     "Choose an option: ")
        if today == "1":
            date = todaysdate()
            break
        elif today== "2":
            date = input("Enter date (YYYY-MM-DD): ").strip()
            if is_valid_date(date):
                break
            print("Invalid date format. Use YYYY-MM-DD.\n")

    # Habit
    while True:
        habit = input("Habit name: ").strip()
        if habit:
            break
        print("Habit can't be empty, try again.\n")

    # Category
    while True:
        category = input("Category (study/fitness/reading/work/other): ").strip().lower()
        if is_valid_category(category):
            break
        print("Invalid category. Try again.\n")

    # Minutes
    while True:
        raw_minutes = input("Enter minutes (integer > 0): ").strip()
        try:
            minutes_value = int(raw_minutes)
            if minutes_value > 0:
                break
            print("Minutes must be > 0.\n")
        except ValueError:
            print("Minutes must be a number.\n")

    # Note
    note = input("Enter note (optional): ").strip()

    # Create session and save
    session = Session(date, habit, category, minutes_value, note)
    tracker.add_session(session)
    print("Session added successfully!\n")

def todays_summary(tracker: HabitTracker):
    ...

def todaysdate():
    texto = asctime(localtime())
    time = texto.split(" ")
    months = {
        "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
        "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
        "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
    }
    day = time[2]
    month = months[time[1]]
    year = time[4]
    date = f"{year}-{month}-{day}"
    return date

if __name__ == "__main__":
    main()