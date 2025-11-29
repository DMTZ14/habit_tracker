from validators import is_valid_category, is_valid_date

class Sessions:
    def __init__(self, date, habit, category, minutes, note):
        if not is_valid_date(date):
            raise ValueError("Invalid date.")
        if not habit.strip():
            raise ValueError("Empty habit.")
        if not is_valid_category(category):
            raise ValueError("Invalid category.")
        if minutes <= 0:
            raise ValueError("Minutes must be > 0.")
        if len(note) > 100:
            raise ValueError("Note too long.")
        self.date = date
        self.habit = habit
        self.category= category
        self.minutes = minutes
        self.note = note
    def __str__(self):
        return f"{self.date}, {self.habit}, {self.category}, {self.minutes}, {self.note} "
