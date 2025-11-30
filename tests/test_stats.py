from models import Session
from stats import (
    total_minutes,
    get_minutes_by_habit,
    get_minutes_by_category,
    get_top_habits,
    get_global_stats,
    best_streak,
)

def _sample_sessions():
    return [
        Session("2025-12-01", "Gym", "fitness", 60, ""),
        Session("2025-12-01", "Python", "study", 45, ""),
        Session("2025-12-02", "Gym", "fitness", 30, ""),
        Session("2025-12-03", "Reading", "reading", 20, ""),
    ]

def test_total_minutes():
    sessions = _sample_sessions()
    assert total_minutes(sessions) == 60 + 45 + 30 + 20

def test_minutes_by_habit():
    sessions = _sample_sessions()
    result = get_minutes_by_habit(sessions)
    assert result["gym"] == 90
    assert result["python"] == 45
    assert result["reading"] == 20

def test_minutes_by_category():
    sessions = _sample_sessions()
    result = get_minutes_by_category(sessions)
    assert result["fitness"] == 90
    assert result["study"] == 45
    assert result["reading"] == 20

def test_top_habits():
    sessions = _sample_sessions()
    top = get_top_habits(sessions, 2)
    assert top[0][0].lower() == "gym"
    assert top[0][1] == 90

def test_best_streak():
    sessions = _sample_sessions()
    # tienes sesiones en 01, 02, 03 → streak de 3 días
    assert best_streak(sessions) == 3

def test_global_stats_not_crashing_on_empty():
    stats = get_global_stats([])
    assert stats["total_minutes"] == 0
    assert stats["total_sessions"] == 0
