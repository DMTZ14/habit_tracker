from models import Session, HabitTracker
from storage import read_sessions
import os

def test_add_session_writes_to_file(tmp_path):
    filepath = tmp_path / "sesiones_test.csv"
    tracker = HabitTracker(filepath=str(filepath))

    s = Session("2025-12-01", "Gym", "fitness", 60, "")

    tracker.add_session(s)

    rows = read_sessions(str(filepath))
    assert rows[0][0] == "2025-12-01"
    assert rows[0][1] == "Gym"
    assert rows[0][2] == "fitness"
