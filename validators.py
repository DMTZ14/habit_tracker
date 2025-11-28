import re
def is_valid_date(txt):
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    return re.search(pattern, txt) is not None

ALLOWED_CATEGORIES = {"study", "fitness", "reading", "work", "other"}
def is_valid_category(cat):
    if cat is None:
        return False
    return cat.strip().lower() in ALLOWED_CATEGORIES
