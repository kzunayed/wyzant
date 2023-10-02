from datetime import date

from statistics import mean
from typing import Any, Dict, List
import data_handling as dh

table = dh.load_csv("turtles_small.csv", header=True)
table = dh.load_csv("turtles_data.csv", header=True)
dh.print_table(table)

rapha_list = [1, 2, 3, 'rapha', 'kazi', 1.0, True, False]
rapha_dictionary = {'age': 30, 'name': 'rapha'}
list_of_dict = [{'name': 'kazi', 'age': 26}, {'name': 'rapha', 'age': 21}]
[{}, {}]
def floatify_column(table: List[Dict[str, Any]], column_name: str) -> None:
    for row in table:
        print(row)

floatify_column(table, 'age')

string = 'dabda 1383 True :)'

def dateify_column(table: List[Dict[str, Any]], column_name: str) -> None:
    pass

def make_estimated_length(table: List[Dict[str, Any]]) -> None:
    pass


def compute_column_mean(table: List[Dict[str, Any]], column_name: str) -> float:
    pass