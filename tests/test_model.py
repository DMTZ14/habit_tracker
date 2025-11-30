from models import Session
import pytest

def test_create_valid_session():
    s = Session("2025-12-01", "Python", "study", 60, "CS50P")
    assert s.date == "2025-12-01"
    assert s.habit == "Python"
    assert s.category == "study"
    assert s.minutes == 60
    assert s.note == "CS50P"

def test_invalid_date_raises():
    with pytest.raises(ValueError):
        Session("2025-13-40", "Python", "study", 60, "")

def test_empty_habit_raises():
    with pytest.raises(ValueError):
        Session("2025-12-01", "   ", "study", 60, "")

def test_invalid_category_raises():
    with pytest.raises(ValueError):
        Session("2025-12-01", "Python", "gaming", 60, "")

def test_negative_minutes_raises():
    with pytest.raises(ValueError):
        Session("2025-12-01", "Python", "study", -10, "")

def test_note_too_long_raises():
    long_note = "a" * 101
    with pytest.raises(ValueError):
        Session("2025-12-01", "Python", "study", 60, long_note)
