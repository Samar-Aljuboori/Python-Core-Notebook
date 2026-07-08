import datetime

def run_datetime_examples():
    print("=== 1. Current Date & Time ===")
    # Get the exact current date and time  ---> now.
    now = datetime.datetime.now()
    print(f"Current Datetime: {now}")
    print(f"Year: {now.year}, Month: {now.month}, Day: {now.day}")
    print(f"Hour: {now.hour}, Minute: {now.minute}, Second: {now.second}")
    print("-" * 50)

    print("=== 2. Creating Specific Dates ===")
    # Create a specific date (Year, Month, Day) ---> datetime.date()
    custom_date = datetime.date(2026, 7, 8)
    print(f"Custom Created Date: {custom_date}")
    print("-" * 50)

    print("=== 3. Formatting Dates (Strftime) ===")
    # Format date into readable strings using format codes ---> now.strftime()
    # %A = Weekday name, %B = Month name, %Y = Year, %d = Day
    formatted_1 = now.strftime("%Y-%m-%d")
    formatted_2 = now.strftime("%A, %B %d, %Y")
    print(f"Standard Format: {formatted_1}")
    print(f"Text Format: {formatted_2}")
    print("-" * 50)

    print("=== 4. Parsing Strings into Dates (Strptime) ===")
    # Convert a normal string into a real Python datetime object  ---> datetime.datetime.strptime()
    date_string = "25/12/2026"
    parsed_date = datetime.datetime.strptime(date_string, "%d/%m/%Y")
    print(f"Converted String to Datetime Object: {parsed_date}")
    print("-" * 50)

    print("=== 5. Time Calculations (Timedelta) ===")
    # Using timedelta to add or subtract time  ---> today + datetime.timedelta ()
    #                                                     -
    today = datetime.date.today()
    ten_days_later = today + datetime.timedelta(days=10)
    five_days_ago = today - datetime.timedelta(days=5)
    
    print(f"Today's Date: {today}")
    print(f"Date 10 Days Later: {ten_days_later}")
    print(f"Date 5 Days Ago: {five_days_ago}")
    print("-" * 50)

    print("=== 6. Calculating Differences Between Dates ===")
    # Calculate how many days are left until a specific event
    new_year_2027 = datetime.date(2027, 1, 1)
    days_remaining = new_year_2027 - today
    print(f"Days remaining until New Year 2027: {days_remaining.days} days")
    print("-" * 50)

if __name__ == "__main__":
    run_datetime_examples()