import csv
import os
DEFAULT_PATH = "data/sesiones.csv"
HEADER = ["date", "habit", "category", "minutes", "note"]
def read_sessions(filepath: str = DEFAULT_PATH):
    if not os.path.exists(filepath):
        return []
    rows = []
    with open(filepath, newline="") as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if not row:
                continue
            if i == 0 and row == HEADER:
                continue
            rows.append(row)
    return rows


def append_session(session, filepath: str = DEFAULT_PATH):
    file_exists = os.path.exists(filepath)
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath,"a",newline="") as f:
        writer=csv.writer(f)
        if not file_exists:
            writer.writerow(HEADER)
        writer.writerow([session.date, session.habit, session.category,session.minutes, session.note])


