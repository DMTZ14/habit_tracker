from time import process_time_ns
from datetime import datetime, timedelta
from models import Session,HabitTracker

def total_minutes(sessions):
    totalmin=0
    for i in sessions:
        totalmin+=i.minutes
    return totalmin

def get_minutes_by_habit(sessions):
    minbyhabit={}
    for i in sessions:
        habit =i.habit.lower()
        if habit not in minbyhabit:
            minbyhabit[habit] = i.minutes
        else:
            minbyhabit[habit] += i.minutes
    return minbyhabit

def get_minutes_by_category(sessions):
    minbycat = {}
    for i in sessions:
        habit = i.category
        if habit not in minbycat:
            minbycat[habit] = i.minutes
        else:
            minbycat[habit] += i.minutes
    return minbycat

def get_top_habits(sessions, n=3):
    habits=get_minutes_by_habit(sessions)
    ordered = sorted(habits.items(), key=lambda x: x[1], reverse=True)
    return ordered[:n]

def get_global_stats(sessions):
    global_stats= {}
    global_stats["total_minutes"]= total_minutes(sessions)
    global_stats["total_sessions"]= len(sessions)
    global_stats["avg_minutes"]= int(round(total_minutes(sessions)/len(sessions),0))
    global_stats["minutes_by_category"] = get_minutes_by_category(sessions)
    global_stats["top_habit"]= get_top_habits(sessions,1)[0]

    return global_stats

def best_streak(sessions):
    dates = sorted(set(s.date for s in sessions))
    parsed = [datetime.strptime(d, "%Y-%m-%d").date() for d in dates]

    max_streak = 1
    current_streak = 1

    for i in range(1, len(parsed)):
        if parsed[i] == parsed[i - 1] + timedelta(days=1):
            current_streak += 1
        else:
            current_streak = 1

        if current_streak > max_streak:
            max_streak = current_streak

    return max_streak

