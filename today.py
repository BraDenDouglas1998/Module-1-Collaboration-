from datetime import date

today = str(date.today())

with open("today.txt", "w") as file:
    file.write(today)


with open("today.txt", "r") as file:
    today_string = file.read()

print(today_string)

from datetime import datetime

parsed_date = datetime.strptime(today_string, "%Y-%m-%d")

print(parsed_date)