# Example module: my_module.py
# def my_function():
#     print("Hello from my_function!")

# In another script:
from test_module import my_function
my_function()


def modify_list(my_list):
    my_list.append(10)
    my_list.sort()

my_list = [5, 3, 8]
modify_list(my_list)
print(my_list)  # This will print the modified list


from typing import Any, Dict, List

def process_data(data: Dict[str, Any]) -> None:
    print(data)
    # Function code here

# Usage:
data: Dict[str, Any] = {'name': 'Alice', 'age': 30}
process_data(data)


import csv
# C:\Users\Anabil\PycharmProjects\scripts\orders.csv
# Reading a CSV file with csv.DictReader
with open('C:/Users/Anabil/PycharmProjects/scripts/orders.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)


from datetime import datetime

# Creating a datetime object
now = datetime.now()
print("Current date and time:", now)

# Formatting a date
formatted_date = now.strftime("%Y-%m-%d")
print("Formatted date:", formatted_date)
