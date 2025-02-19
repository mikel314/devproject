from datetime import datetime


def days_between_dates(date1, date2):
    """
    Calculate the number of days between two dates.

    Parameters:
    date1 (str): The first date in the format 'YYYY-MM-DD'.
    date2 (str): The second date in the format 'YYYY-MM-DD'.

    Returns:
    int: The number of days between the two dates.
    """
    date1_parsed = datetime.strptime(date1, "%Y-%m-%d")
    date2_parsed = datetime.strptime(date2, "%Y-%m-%d")
    return abs((date2_parsed - date1_parsed).days)


a = 1
print("Hello World!")
print("How are you?")
print(a)
a = a + 1
print("Doing well?")
print("Good bye World!")
a = a + 1
print(a)

# Example usage
date1 = "2025-02-18"
date2 = "2025-03-01"
print(days_between_dates(date1, date2))  # Output: 11


def add(a, b):
    return a + b


b = 1
print("Testing new branch in git!")
b = b + a
print(b)
