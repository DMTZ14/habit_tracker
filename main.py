from models import Session, HabitTracker
from stats import total_minutes, get_minutes_by_habit, get_top_habits, get_global_stats, get_minutes_by_category, \
    best_streak
from validators import is_valid_date, is_valid_category
from datetime import date
import os


def main():
    tracker = HabitTracker()
    while True:
        choice= menu()
        print()
        if choice =="1":
            handle_add_session(tracker)
        elif choice =="2":
            handle_todays_summary(tracker)
        elif choice =="3":
            handle_range_summary(tracker)
        elif choice =="4":
            handle_global_statistics(tracker)
        elif choice=="5":
            handle_export_summary(tracker)
        elif choice =="6":
            print("Goobye!\n")
            break
        else:
            print("=== Choice out of range ===\n")

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

def todaysdate() -> str:
    return date.today().isoformat()

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
        habit = input("Habit name: ").strip().capitalize()
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

def handle_todays_summary(tracker: HabitTracker):
    today = todaysdate()
    todays_sessions=tracker.get_sessions_by_date(today)
    if not todays_sessions:
        print(f"No sessions found for today ({today}).\n")
        return

    print(f"=== Today's Summary ({today}) ===")

    for i in todays_sessions:
        print(f"{i.habit.title()} ({i.category}): {i.minutes} min.")

    print(f"\nTotal today: {total_minutes(todays_sessions)}\n")

def handle_range_summary(tracker: HabitTracker):
    start_date= input("Enter start date YYYY-MM-DD: ").strip()
    end_date = input("Enter end date YYYY-MM-DD: ").strip()

    #Validate dates format
    try:
        range_sessions = tracker.get_sessions_by_range(start_date, end_date)
    except ValueError as e:
        print(f"Error: {e}\n")
        return
    #Validate sessions exist
    if not range_sessions:
        print(f"No sessions found between {start_date} and {end_date}.\n")
        return

    print(f"=== Summary from {start_date} to {end_date} ===\n")

    #Habits & minutes
    ranged_min_by_habit= get_minutes_by_habit(range_sessions)
    for i in ranged_min_by_habit:
        print(f"{str(i).title()}: {ranged_min_by_habit[i]} min")
    print()
    #Top Habits
    print("Top 3 habits:")
    ranged_top_habits = get_top_habits(range_sessions)
    ind=1
    for i in ranged_top_habits:
        session = list(i)
        print(f"{ind}) {str(session[0]).title()} - {session[1]} min")
        ind+=1
    print()

    print(f"Total in range: {total_minutes(range_sessions)} minutes.\n")

def handle_global_statistics(tracker: HabitTracker):
    all_sessions= tracker.get_all_sessions()
    if not all_sessions:
        print("No sessions recorded yet.")
        return
    print("=== Global Statistics ===")
    #Global stats
    global_stats = get_global_stats(all_sessions)
    print(
        f"Total sessions: {global_stats['total_sessions']}\n"
        f"Total minutes: {global_stats['total_minutes']}\n"
        f"Average minutes by session: {global_stats['avg_minutes']}\n"
    )
    #Minutes by category
    print("Minutes by category")
    min_by_cat= get_minutes_by_category(all_sessions)
    for i in min_by_cat:
        print(f"{str(i).title()}: {min_by_cat[i]}")
    print()

    #Top Habit
    print("Top habit")
    top_habit= list(get_top_habits(all_sessions,1)[0])
    print(f"{str(top_habit[0]).title()} - {top_habit[1]} min\n")

    #Best streak
    print(f"Best streak: {best_streak(all_sessions)} days\n")

def handle_export_summary(tracker: HabitTracker):
    start_date= input("Enter start date YYYY-MM-DD: ")
    end_date = input("Enter end date YYYY-MM-DD: ")
    os.makedirs("reports", exist_ok=True)
    file_name= f"reports/report_{start_date}_{end_date}.txt"

    try:
        all_sessions = tracker.get_sessions_by_range(start_date, end_date)
    except ValueError as e:
        print(f"Error: {e}\n")
        return

    #Validate sessions exist
    if not all_sessions:
        print(f"No sessions found between {start_date} and {end_date}. Report not created.\n")
        return

    with open(file_name,"w") as file:
        file.write(f"HabitForge – Summary Report\n"
                   f"Range: {start_date} to {end_date}\n\n")

        # Habits & minutes
        ranged_min_by_habit = get_minutes_by_habit(all_sessions)
        for i in ranged_min_by_habit:
            file.write(f"{str(i).title()}: {ranged_min_by_habit[i]} min\n")

        # Top Habits
        file.write("\nTop 3 habits:\n")
        ranged_top_habits = get_top_habits(all_sessions)
        ind = 1
        for i in ranged_top_habits:
            session = list(i)
            file.write(f"{ind}) {str(session[0]).title()} - {session[1]} min\n")
            ind+=1

        file.write(f"\nTotal in range: {total_minutes(all_sessions)} minutes.\n")

    print(f"Report saved to: reports/report_{start_date}_{end_date}.txt\n")


if __name__ == "__main__":
    main()