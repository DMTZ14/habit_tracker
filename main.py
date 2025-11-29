'''
from models import HabitTracker, Session
from validators import is_valid_date, is_valid_category
from stats import (
    get_minutes_by_habit,
    get_minutes_by_category,
    get_top_habits,
    get_global_stats,
)
import datetime
'''

def main():
      menu()

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
            end=""
      )
      return input().strip()


if __name__ == "__main__":
      main()