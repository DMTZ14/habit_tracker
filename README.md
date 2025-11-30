# HabitForge – CLI Habit Tracker
HabitForge is a small command-line application to track daily habits and see how consistent you
really are.
You can log sessions for things like **Python study**, **gym**, **reading**, **running**, etc.
The app stores your sessions in a CSV file, computes useful statistics, and can export a text
report.
I built this as a learning project to practice:
- Python syntax and the standard library
- OOP (classes, methods, encapsulation)
- File I/O with CSV
- Basic data analysis on lists of objects
- Error handling and input validation
- Writing tests with `pytest`
---
## Features
- **Add new session**
 - Date (default: today)
 - Habit name (e.g. `Python`, `Gym`, `Reading`)
 - Category: `study`, `fitness`, `reading`, `work`, `other`
 - Minutes: positive integer
 - Optional note (max 100 characters)
 - Input is validated before saving.
- **Today’s summary**
 - Shows all sessions for today.
 - Displays minutes per habit and total minutes for today.
- **Summary by date range**
 - Asks for `start` and `end` dates.
 - Aggregates total minutes per habit in that range.
 - Shows the **top 3 habits** and total minutes in that range.
- **Global statistics**
 - Total minutes (all time)
 - Total number of sessions
 - Average minutes per session
 - Minutes by category
 - Top habit (by total minutes)
 - Best streak of consecutive days with at least one session
- **Export summary to file**
 - Asks for a date range.
 - Generates a `.txt` report under `reports/` with:
 - Range information
 - Minutes by habit
 - Top 3 habits
 - Total minutes in that range
- **Graceful error handling**
 - Invalid dates are rejected (format + real calendar dates).
 - Categories must be one of the allowed values.
 - Minutes must be an integer greater than 0.
 - If there are no sessions for a given date/range, the app tells you instead of crashing.
---
## Data Model
### `Session`
Represents a single block of time dedicated to a habit:
```python
Session(
 date="2025-12-01",
 habit="Python",
 category="study",
 minutes=45,
 note="CS50P"
)
```
Validation inside the constructor ensures that:
- The date is valid (`YYYY-MM-DD` and a real calendar date)
- The habit name is not empty
- The category is one of (`study`, `fitness`, `reading`, `work`, `other`)
- `minutes` is an `int > 0`
- `note` is at most 100 characters
### `HabitTracker`
Responsible for:
- Loading sessions from a CSV file
- Adding new sessions and writing them to disk
- Returning sessions:
 - for all time
 - for a specific date
 - for a date range
---
## Project Structure
```text
.
■■■ main.py # CLI entry point and menu handlers
■■■ models.py # Session & HabitTracker classes
■■■ stats.py # Aggregations and statistics
■■■ storage.py # CSV read/write helpers
■■■ validators.py # Date & category validation
■■■ data/
■ ■■■ sesiones.csv # Created automatically on first run
■■■ reports/ # Text reports are saved here
■■■ tests/
 ■■■ test_model.py
 ■■■ test_stats.py
 ■■■ test_storage_tracker.py
```
`data/` and `reports/` are created automatically if they don’t exist.
---
## Requirements
- Python 3.10+ (tested on 3.13)
- `pytest` for running the tests (`pip install pytest`)
- No external libraries are used in the app itself; everything is standard library.
---
## Installation
Clone the repository and create a virtual environment:
```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
python -m venv .venv
source .venv/bin/activate # On Windows: .venv\Scripts■ctivate
```
(Optional) Install `pytest` for testing:
```bash
pip install pytest
```
---
## Running the App
From the project root:
```bash
python main.py
```
You’ll see a menu like:
```text
=== HabitForge: Habit Tracker ===
1. Add new session
2. View today's summary
3. View summary by date range
4. View global statistics
5. Export summary to file
6. Exit
Choose an option:
```
---
## Running Tests
From the project root:
```bash
pytest
```
---
## Possible Future Improvements
- Edit or delete existing sessions from the CLI
- Allow custom tags in addition to the fixed categories
- Add a “quick add” command, for example:
 ```bash
 python main.py quick "Python" 30
 ```
- Export stats to JSON or Markdown
- Simple charts (ASCII or via another tool)
---
## License
No explicit license yet. You are welcome to read and use the code for learning purposes.