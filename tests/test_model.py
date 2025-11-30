import pytest
from models import Session

def test_create_session():
    s = Session("2025-11-30","Meditar","other",30,"")
    assert s.date =="2025-11-30"
    assert s.habit == "Meditar"
    assert s.category =="other"
    assert s.minutes == 30
    assert s.note == ""

def test_invalid_date():
    with pytest.raises(ValueError):
        Session("2025-13-400", "Python", "study", 60, "")

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