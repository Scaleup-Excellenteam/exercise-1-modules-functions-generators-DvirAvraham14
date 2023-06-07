import random
from datetime import datetime, timedelta

date_in1 = input("Enter the first date in the format YYYY-MM-DD: ")
date_in2 = input("Enter the second date in the format YYYY-MM-DD: ")

date1_obj = datetime.strptime(date_in1, "%Y-%m-%d")
date2_obj = datetime.strptime(date_in2, "%Y-%m-%d")

delta = date2_obj - date1_obj
random_days = random.randrange(delta.days)  # random days between 0 and delta
new_date = date1_obj + timedelta(days=random_days)  # add random days

if new_date.weekday() == 0:
    print("I have no vinaigrette!")

print("The new date is:", new_date.strftime("%Y-%m-%d"))
