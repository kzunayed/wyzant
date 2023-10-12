# Practice Set 06: What's *in* a name?

import csv
import re
from datetime import date
from pprint import pprint
from sys import stderr
from typing import Dict, List

# Part 1: RegexOne Tutorial
# -------------------------

# The following problems mirror the problems in the RegexOne tutorials:
# https://regexone.com/lesson/introduction_abcs


def lesson_1(input_string):
    pattern = r"abc"
    return re.search(pattern, input_string)


def lesson_1_and_a_half(input_string: str):
    # https://regexone.com/lesson/letters_and_digits
    pattern = r"\d"
    return re.search(pattern, input_string)


def lesson_2(input_string: str):
    # https://regexone.com/lesson/wildcards_dot
    pattern = r"...\."
    return re.search(pattern, input_string)


def lesson_3(input_string: str):
    # https://regexone.com/lesson/matching_characters
    pattern = r"[cmf]an"
    return re.search(pattern, input_string)


def lesson_4(input_string: str):
    # https://regexone.com/lesson/excluding_characters
    pattern = r"[^b]og"
    return re.search(pattern, input_string)


def lesson_5(input_string: str):
    # https://regexone.com/lesson/character_ranges
    pattern = r"[A-Z][n-p][a-c]"
    return re.search(pattern, input_string)


def lesson_6(input_string: str):
    # https://regexone.com/lesson/repeating_characters
    pattern = r"waz{3,5}up"
    return re.search(pattern, input_string)


def lesson_7(input_string: str):
    # https://regexone.com/lesson/kleene_operators
    pattern = r"aa+b*c+"
    return re.search(pattern, input_string)


def lesson_8(input_string: str):
    # https://regexone.com/lesson/optional_characters
    pattern = r"\d+ files? found\?"
    return re.search(pattern, input_string)


def lesson_9(input_string: str):
    # https://regexone.com/lesson/whitespaces
    pattern = r"\d\.\s+abc"
    return re.search(pattern, input_string)


def lesson_10(input_string: str):
    # https://regexone.com/lesson/line_beginning_end
    pattern = r"^Mission: successful$"
    return re.search(pattern, input_string)


def lesson_11(input_string: str):
    # https://regexone.com/lesson/capturing_groups
    pattern = r"^(file.+)\.pdf$"

    if m := re.search(pattern, input_string):
        return m.group(1)


def lesson_12(input_string: str):
    # https://regexone.com/lesson/nested_groups
    pattern = r"(\w+ (\d+))"

    if m := re.search(pattern, input_string):
        return m.group(1), m.group(2)


def lesson_13(input_string: str):
    # https://regexone.com/lesson/more_groups
    pattern = r"(\d+)x(\d+)"

    if m := re.search(pattern, input_string):
        return m.group(1), m.group(2)


def lesson_14(input_string: str):
    # https://regexone.com/lesson/conditionals
    pattern = r"I love (cats|dogs)"
    return re.search(pattern, input_string)


def lesson_15(input_string: str):
    # https://regexone.com/lesson/misc_meta_characters
    pattern = r".*"
    return re.search(pattern, input_string)


# Part 2: Data Validation
# -----------------------

def validate_street_address(address: str) -> str:
    stripped_address = address.strip()
    # makes sure string begins with a digt
    if stripped_address[0].isdigit():
        # makes sure there are letters in string
        if re.search('[a-zA-Z]', stripped_address):
            return address
        else:
            return ''
    else:
        return ''


def validate_name(name: str) -> str:
    stripped_name = name.strip()
    # Pattern begins with letter and may contain certain special characters. Repeated for middle name optionally. Same for last name
    pattern = r"^[A-Za-z.'-]+\s[A-Za-z.'-]*\s?[A-Za-z.'-]+$"

    if re.match(pattern, stripped_name):
        return stripped_name
    else:
        return ''


def validate_email(email: str) -> str:
    stripped_email = email.strip()
    if stripped_email not in (' '):
        # Pattern included alphanumeric char before '@' followed by more alphanumeric/symbols before '.' followed by letters only
        pattern = r'^[a-zA-Z0-9]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$'
        match = re.match(pattern, stripped_email)
        if match:
            return stripped_email
        else:
            return ''
    else:
        return ''

def validate_phone_number(phone_number: str) -> str:
    # replace non digit characters with empty space
    phone_number = re.sub(r"\D", "", phone_number)
    if len(phone_number) == 10:
        return phone_number
    else:
        return ''


def validate_state(state: str) -> str:
    # converts argument to uppercase so no worrying about casing
    state = state.upper()
    if state in ('IN', 'INDIANA'):
        return 'IN'
    else:
        return ''


def validate_zip_code(code: str) -> str:
    # opening file
    with open('extra_data/indiana_zip_codes.txt', 'r') as file:
        # reading lines
        lines = file.readlines()
        zip_codes = []
        # iterating over lines and appending them to list
        for line in lines:
            zip_code = line.strip()
            zip_codes.append(zip_code)
        if code in zip_codes:
            return code
        else:
            return ''


def validate_date(iso_date: str) -> str:
    try:
        if date.fromisoformat(iso_date):
            return iso_date
    except:
        return ''


def validate_row(row: Dict[str, str]) -> Dict[str, str]:
    """Validate a row of customer data.

    All fields are required, so empty string `''` implies an error.
    """
    return {
        "name": validate_name(
            row.get("first_name", "") + " " + row.get("last_name", "")
        ),
        "email": validate_email(row.get("email", "")),
        "phone_number": validate_phone_number(row.get("phone_number", "")),
        "event_date": validate_date(row.get("event_date", "")),
        "billing_address": validate_street_address(row.get("billing_address", "")),
        "state": validate_state(row.get("state", "")),
        "zip_code": validate_zip_code(row.get("zip_code", "")),
    }


def standardize_and_validate() -> List[Dict[str, str]]:
    """Standardize and validate the contents of `customer_data.csv`.

    On failure, print the row number and raise `SystemExit(1)`.
    """

    with open("customer_data.csv") as csvfile:
        data = [row for row in csv.DictReader(csvfile)]

    standardized = []
    for i, row in enumerate(data, start=2):
        new_row = validate_row(row)
        if any((v == "" or v is None) for v in new_row.values()):
            print(
                f"Row {i}: failed validation/standardization. Found empty string:",
                file=stderr,
            )
            pprint(
                {k: v for k, v in new_row.items() if (v == "" or v is None)},
                stream=stderr,
            )
            print(f"Row {i} originally contained:", file=stderr)
            pprint(data[i - 2], stream=stderr)

            raise SystemExit(1)

        # Otherwise: append the standardized row.
        standardized.append(new_row)

    return standardized


def main():
    """Standardize `customer_data.csv`, then write it to `standardized_data.csv`.

    If a row fails validation: print keys that return `''` and exit.
    """

    # Program halts immediately if standardization/validation fails.
    standardized = standardize_and_validate()

    print("Writing results to `standardized_data.csv`")
    with open("standardized_data.csv", "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=standardized[0].keys())
        writer.writeheader()
        writer.writerows(standardized)


if __name__ == "__main__":
    main()
