class Sessions:
    def __init__(self, date, habit, category, minutes, note):
        self.date = date
        self.habit = habit
        self.category= category
        self.minutes = minutes
        self.note = note

date: str

habit: str

category: str

minutes: int

note: str | None