from validators import is_valid_category, is_valid_date
from storage import append_session, read_sessions, DEFAULT_PATH, HEADER

class Session:
    def __init__(self, date: str, habit: str, category: str, minutes: int, note: str = ""):
        if not is_valid_date(date):
            raise ValueError("Invalid date.")
        if not habit or not habit.strip():
            raise ValueError("Empty habit.")
        if not is_valid_category(category):
            raise ValueError("Invalid category.")
        if not isinstance(minutes, int) or minutes <= 0:
            raise ValueError("Minutes must be > 0.")
        if note is None:
            note = ""
        if len(note) > 100:
            raise ValueError("Note too long.")

        self.date = date.strip()
        self.habit = habit.strip()
        self.category = category.strip().lower()
        self.minutes = minutes
        self.note = note.strip()

    def __str__(self) -> str:
        return f"{self.date},{self.habit},{self.category},{self.minutes},{self.note}"

class HabitTracker:
    def __init__(self, filepath: str = DEFAULT_PATH):
        self.filepath = filepath
        self.sessions: list[Session] = []
        self._load_from_file()

    def _load_from_file(self) -> None:
        rows = read_sessions(self.filepath)
        for row in rows:
            if len(row) != 5:
                continue

            date, habit, category, minutes_str, note = row

            try:
                minutes = int(minutes_str)
                session = Session(date, habit, category, minutes, note)
            except ValueError:
                continue

            self.sessions.append(session)

    def add_session(self, session: Session):
        self.sessions.append(session)
        append_session(session)

    def get_all_sessions(self):
        return list(self.sessions)


