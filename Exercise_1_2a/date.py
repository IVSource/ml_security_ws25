import re
from datetime import datetime

def validate_datestring(datestring: str) -> bool:
    """
    Validate a date in the format "2025-9-17" by the rules:
    - Only numbers and dashes are allowed.
    - Leading zeros are optional.
    - Must be between 8 and 10 characters.
    """
    pattern = r"^[0-9-]{8,10}$"
    return re.match(pattern, datestring) is not None

def print_date(datestring: str) -> None:
    if validate_datestring(datestring):
        print(f"✅ '{datestring}' is a valid date. The date interpreted is: ")
        the_date = datetime.strptime(datestring, "%Y-%m-%d")
        print(f"{str(the_date)}")
    else:
        print(f"❌ '{datestring}' is NOT a valid date.")

def main():
    datestring = input("Enter a date in the format YYYY-MM-DD: ").strip(' \t\r\n')
    print_date(datestring)

if __name__ == "__main__":
    main()
