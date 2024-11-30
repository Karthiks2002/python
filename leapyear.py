day=int(input("Enter the day (1-31):"))
month=int(input("Enter the month (1-12):"))
year=int(input("Enter the year"))

print(f"Entered date:{day:02d}-{month:02d}-{year}")
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")