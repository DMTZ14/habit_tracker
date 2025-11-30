import re
from datetime import datetime

def is_valid_date(txt):
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    if not re.search(pattern, txt):
        return False
    try:
        datetime.strptime(txt, "%Y-%m-%d")
        return True
    except ValueError:
        return False
ALLOWED_CATEGORIES = {"study", "fitness", "reading", "work", "other"}
def is_valid_category(cat):
    if cat is None:
        return False
    return cat.strip().lower() in ALLOWED_CATEGORIES
