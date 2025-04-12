# Employee data with fixed days off
EMPLOYEES = [
    {"name": "Jackie", "department": "Marketing", "fixed_off": "Sunday"},
    # ... (paste the full list from earlier)
]

# Shift definitions
SHIFTS = {
    "D": {"name": "Day", "hours": "6:00-15:00", "min_staff": 3, "max_staff": 4},
    # ... (other shifts)
}

# Special day requirements
SPECIAL_DAYS = {
    "Monday": {"D": 4, "M": 3, "N": 3},
    "Thursday": {"D": 3, "M": 5, "N": 3}
}

# Valid shift patterns
VALID_PATTERNS = [
    ["D", "OFF", "D"],
    # ... (other patterns)
]
