def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        
        except ValueError:
            print("❌ ❌ Please enter a valid number!")

years = get_float("how Old ar yoy? Enter a number:  ")

def calculate_minutes(total_years):
    DAYS_IN_YEAR = 365.25
    HOURS_IN_DAY = 24
    MINUTES_IN_HOUR = 60

    total_days = round(total_years * DAYS_IN_YEAR)
    total_hours = round(total_days * HOURS_IN_DAY)
    total_minutes = round(total_hours * MINUTES_IN_HOUR)

    return f"\nYou data is \n - Total days is {total_days} \n - Total hours is {total_hours} \n - Total minutes is {total_minutes} "

print(calculate_minutes(years))


