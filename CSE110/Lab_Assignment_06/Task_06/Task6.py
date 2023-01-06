days = int(input())

def date_calculator(days):
    years = days // 365
    months = (days % 365) // 30
    days = (days % 365) % 30
    print(years, "years,", months, "months,", days, "days")

date_calculator(days)