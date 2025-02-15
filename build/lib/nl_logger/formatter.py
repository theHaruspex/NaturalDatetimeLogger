import logging
from datetime import datetime


class NaturalLanguageFormatter(logging.Formatter):
    """Custom logging formatter to display timestamps in natural language format."""

    def formatTime(self, record, datefmt=None):
        dt = datetime.fromtimestamp(record.created)

        # Get the day of the month
        day = dt.day

        # Determine the correct suffix for the day
        if 11 <= day <= 13:
            suffix = "th"
        else:
            suffix = {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")

        # Format the time with the suffix
        return dt.strftime(f"%I:%M:%S%p, %B {day}{suffix}")