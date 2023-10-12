# PS-06: What's _in_ a name?

## Overview

There's a final topic for us to explore purely on the Python side before diving into web applications: **data validation** and **data standardization**.

An organization that does Indiana event planning contacted you and sent `customer_data.csv`. It's pretty good, but inconsistencies will make it difficult to work with.

For example, the first few lines alone make it obvious that phone numbers were never standardized:

|first_name|last_name |email                  |phone_number  |event_date|billing_address      |state  |zip_code|credit_card_number|email_confirmed|
|----------|----------|-----------------------|--------------|----------|---------------------|-------|--------|------------------|---------------|
|Artus     |Tunbridge |atunbridge0@uiuc.edu   |(260) 127-8269|2023-07-27|5 Del Sol Street     |Indiana|46862   |5048374116399595  |0              |
|Kalie     |Kew       |kkew1@home.pl          |765-970-1405  |2023-08-30|3 Darwin Parkway     |Indiana|47905   |5048375427195010  |1              |
|Humbert   |Antonomoli|hantonomoli2@smh.com.au|(812) 167 1035|2022-07-11|0355 Rockefeller Park|Indiana|47805   |                  |0              |
|Saul      |Marran    |smarran3@issuu.com     |5746292751    |2023-02-06|29 Badeau Alley      |Indiana|46634   |                  |1              |
|Marion    |McIlvenna |mmcilvenna4@webs.com   |260-241-3947  |2022-09-28|30 Cardinal Street   |Indiana|46867   |                  |0              |

### 🥅 Goals

We need to tidy up our data set.

There is a *some* new material concerning regular expressions, but this assignment will require all the skills you've gained so far. We will:

- Write regular expressions with the `re` module
- Anticipate consequences of design choices
- Validate inputs to test whether they *meet* design choices
- Standardize inputs to enforce data consistency
- Return error responses when we do not have enough information to make a decision
- Standardize and validate `customer_data.csv` for use in Project 2.1

### ✅ Checking solutions are correct

We've included a `test_submission.py` with unit tests to help check whether functions are meeting expectations.

You can run all unit tests by invoking the file in the terminal:

```console
$ python3 test_submission.py
................
----------------------------------------------------------------------
Ran 580 tests in 0.084s

OK
```

That's a lot of tests. You might also want to skim the Visual Studio Code guide on Python Testing: https://code.visualstudio.com/docs/python/testing

## Regular Expression Playground

You may find it helpful to work in an *interactive* regular expression playground.

You might like [Regex101](https://regex101.com/), just be sure to use *Python*-mode, or the expressions may not behave correctly!

![Screenshot of the regex101 site, highlighting Python, the \d regular expression, four matches, and highlighted 0, 1, 2, and 3, while a, b, c, d, are ignored.](./docs/regex101highlights.jpg)

## Practice Problems

### PS-06-01

First we need to practice writing **regular expressions**. There are fifteen problems in this interactive tutorial:

[**https://regexone.com/**](https://regexone.com/)

As you solve each of the fifteen problems, add your solution to each "lesson" function. Replace:

```python
pattern = r""
```

with your solution. For `lesson_1()`, you might write:

```python
def lesson_1(input_string):
    pattern = r"abc"
    return re.search(pattern, input_string)
```

Note: the "r" prefix refers to a "raw" Python string. The TL;DR explanation (Too Long; Didn't Read) version is that a Python raw string interprets special characters like '\\' as actual strings, whereas the default strings we've used up to this point sometimes use those special characters to mark things like tabs ('\t') or newlines ('\n'). See also: [https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals](https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals)

### ✅ Tests

```bash
python3 test_submission.py -k PS_06_01
```

---

### PS-06-02

Let's start with `billing_address`. Addresses start with a number; then contain a combination of letters, numbers, spaces, hyphens, commas, and periods. These things are addresses:

```text
195 Macpherson Junction
9 Pleasure Point
        9 Pleasure Point
85 Market-Place Road
95 St. Matthews Street
385 Westerfield Way, Apt. 12
    385 Westerfield Way, Apartment 12
80 Maryland Plaza, PO Box 1234
  25 51st Street
```

... and these are not:

```
Alexander L. Hayes
195
9-
1.
2021-11-14
PO Box 1234
```

Implement `validate_street_address(address: str)`.

For strings containing addresses, it should return the relevant portion:

```python
>>> validate_street_address("195 Macpherson Junction")
'195 Macpherson Junction'

>>> validate_street_address("  25 51st Street       ")
'25 51st Street'
```

... but for **non**-valid addresses, it should return the empty string:

```python
>>> validate_street_address("195")
''

>>> validate_street_address("2021-11-14")
''
```

<details>
<summary><strong>Hint #1</strong>: Our addresses always start with a number</summary>

> [Lesson 1.5](https://regexone.com/lesson/letters_and_digits) discussed matching digits:
>
> ```python
> import re
>
> print(re.match("\d+"))
> ```

</details>

<details>
<summary><strong>Hint #2</strong>: Matching specific characters</summary>

> [Lesson 3](https://regexone.com/lesson/matching_characters) showed how to match specific characters using the bracket `[]` syntax.
>
> And addresses may contain: letters, numbers, spaces, hyphens, commas, and periods.

</details>

<details>
<summary><strong>Hint #3</strong>: Don't forget about Python!</summary>

> Regular expressions are great for matching text, but they aren't always the easiest.
>
> Sometimes a simple `.strip()` is *much* easier when dealing with spacing:
>
> ```python
> >>> word = "      bagel     "
> >>> print(word)
> '      bagel     '
> >>> print(word.strip())
> 'bagel'
> ```

</details>


### ✅ Tests

```bash
python3 test_submission.py -k PS_06_02
```

---

### PS-06-03

Let's explore a side path: the risk of *over-validation* and the real-world consequences that *over-validation* can have on people.

[![YouTube preview of Dylan Beattie GOTO 2023 talk on Plain Text, starting from 18:59 and his Magnus Martensson example.](./docs/youtube_preview_beattie_2023_plain.jpg)](https://www.youtube.com/watch?v=4mRxIgu9R70&t=1134s)

Write a function: `validate_name(name: str) -> str`, and explain your implementation choices in a docstring.

### ✅ Tests

No tests. But consider how your implementation behaves for cases like the following:

```python
>>> validate_name("Alexander L. Hayes")

>>> validate_name("Erika Biga Lee")

>>> validate_name("姜峯楠")

>>> validate_name("Magnus Mårtensson")
```

---

### PS-06-04

Email addresses are hard to validate for a completely different reason: *no one actually agrees on how email should work*.

[![YouTube preview of Dylan Beattie NDC 2023 talk on Email vs Capitalism, starting from 20:48 to discuss what the email specification states versus what email providers actually implement.](./docs/youtube_preview_beattie_2022_email.jpg)](https://youtu.be/mrGfahzt-4Q?si=SFEkwPjW9mimvmUo&t=1244)

Here's what pretty much everyone does in practice:

1. A user signs up with something that *looks* like an email
2. The back end negotiates with an email system
3. An email is generated and sent to the email address via the email system
4. The user is told to "*Please click the link in the email we just sent you*"
5. The act of *clicking the link* is where validation actually occurs

Steps 2-5 are hard, so let's *only* focus on step (1).

These look like valid email addresses:

```
hayesall@iu.edu
       hayesall@iu.edu
pschulze1e@w3.org
rheavyside1g@bbc.co.uk
mzeplink5@over-blog.com
```

... and these do **not** look like email addresses:

```
hayesall
@h.com
@
@.
.
alexander hayes@iu.edu
hayesall@hayesall.c om
h @ c . c
```

Implement `validate_email(email: str)`. It should return an email address, or the empty string otherwise:

```python
>>> validate_email("hayesall@iu.edu")
'hayesall@iu.edu'

>>> validate_email("       rheavyside1g@bbc.co.uk")
'rheavyside1g@bbc.co.uk'

>>> validate_email('@h.com')
''

>>> validate_email("hayesall@ha yesall.com")
''
```

### ✅ Tests

```bash
python3 test_submission.py -k PS_06_04
```

---

### PS-06-05

The client wants to focus on 10-digit "United States"-based phone numbers. Users, however, each have their own idiosyncratic way of writing a phone number. Let's assume that these are fine:

```text
(313)4843685
769-690-6887
(212) 879-1973
(203)365-1285
```

... but these are too ambiguous to handle:

```text
9--
(020)30129991059189
808611784989191877
a20-903-629103
```

When a phone number is okay, we should *standardize* it to only include the digits. Or we should return the empty string when the input is invalid:

```python
>>> validate_phone_number("(571) 359 6273")
'5713596273'

>>> validate_phone_number("(020)30129991059189")
''
```

<details>
<summary><strong>Hint</strong>: Is regex necessary?</summary>

> The Python `re` module has a powerful [`re.sub`](https://docs.python.org/3/library/re.html#re.sub) method, which can replace characters in a string. For example: what if you want to replace every number with an underscore?
>
> ```python
> >>> import re
> >>> original = "A 1 B 2 C 3 D 4"
> >>> re.sub(r"\d", "_", original)
> 'A _ B _ C _ D _'
> ```
>
> *But*: you may be more comfortable with the [`.replace()`](https://docs.python.org/3/library/stdtypes.html#str.replace) method, or you you might have previously used [`.isdigit()`](https://docs.python.org/3/library/stdtypes.html#str.isdigit).

</details>


### ✅ Tests

```bash
python3 test_submission.py -k PS_06_05
```

---

### PS-06-06

The client is only authorized to work with customers who have Indiana billing addresses, so let's write `validate_state(state: str) -> str` to validate and standardize that the input looks like *Indiana*. When the input is okay, let's return the `IN` postal code; and the empty string otherwise.

```python
>>> validate_state("Indiana")
'IN'

>>> validate_state('in')
'IN'

>>> validate_state('indiana')
'IN'

>>> validate_state('Wyoming')
''
```

### ✅ Tests

```bash
python3 test_submission.py -k PS_06_06
```

---

### PS-06-07

Similarly, only Indiana zip codes are valid here. Luckily, the client gave you a copy of them in `extra_data/indiana_zip_codes.txt`.

Write `validate_zip_code(code: str) -> str` to return the zip code string when it is valid, and empty string otherwise:

```python
>>> validate_zip_code("47406")
'47406'

>>> validate_zip_code("76206")
''
```

### ✅ Tests

```bash
python3 test_submission.py -k PS_06_07
```

---

### PS-06-08

Finally, `validate_date(iso_date: str) -> str` should take an ISO-standard date string (e.g. "2020-01-01"), return the string when the date is valid, and empty string otherwise.

```python
>>> validate_date("2000-05-14")
'2000-05-14'

>>> validate_date("2014-02-31")
''

>>> validate_date("February 23rd, 2022")
''
```

<details>
<summary><strong>Hint #1</strong>: We already saw this in PS-05-03</summary>

> In Practice Set 05, we already saw:
>
> ```python
> >>> from datetime import date
> >>> date.fromisoformat("2023-01-01")
> datetime.date(2023, 1, 1)
> ```
>
> But now it would be helpful to identify what can happen when date parsing goes wrong.
>
> ```python
> >>> date.fromisoformat("2014-02-31")
> ```

</details>

<details>
<summary><strong>Hint #2</strong>: try/except is dangerous, but ...</summary>

> try/except is dangerous, but sometimes we're forced to use it because it's the only built-in option that Python has.
>
> Remember, be *precise* about the error you want to catch. A poorly written try/except block can lead to unexpected code paths propogating through the execution: resulting in code that is nearly impossible to debug.
>
> If you can *anticipate* a `ValueError` is about to occur, you can reduce the likelihood dangerous side effects by
>
> 1. being precise about the type of error you know how to handle
> 2. limiting the exception scope as much as possible
>
> ```python
> x = "hayesall"
>
> try:
>     x = float(x)
> except ValueError:
>     x = None
>
> print(x)
> ```

</details>

### ✅ Tests

```bash
python3 test_submission.py -k PS_06_08
```

---

### PS-06-09

Three functions were implemented for you: `validate_row`, `standardize_and_validate`, and `main`.

Un-comment the `if __name__ == "__main__"` lines at the bottom of your Python starter file with <kbd>^ Ctrl</kbd> + <kbd>/</kbd> or <kbd>Cmd ⌘</kbd> + <kbd>/</kbd>. Running the script with `python3 submission.py` should now produce a new file: `standardized_data.csv`.

We recommend committing a copy of `standardized_data.csv` here; it will be a good starting point for Project 2.1.

### ✅ Tests

```bash
python3 test_submission.py -k PS_06_09
python3 test_submission.py
```

---

## Rubric

- Code that runs without errors and meets all requirements will initially receive full points
- Code that does *not* run will receive a maximum of 50%
- Code will lose a point if it is not sufficiently commented. At a minimum: functions should have a short docstring explaining the function purpose, and code with non-obvious behavior should have an inline comment.
- Code that is *over-commented* will receive a maximum of 50%

| | Maximum Points | Commenting? | Functionality? |
| -----: | :----: | :----: | :-----: |
| PS_06_01 | 3 | 1 | 2 |
| PS_06_02 | 3 | 1 | 2 |
| PS_06_03 | 3 | 2 | 1 |
| PS_06_04 | 4 | 1 | 3 |
| PS_06_05 | 3 | 1 | 2 |
| PS_06_06 | 3 | 1 | 2 |
| PS_06_07 | 3 | 1 | 2 |
| PS_06_08 | 4 | 1 | 3 |
| PS_06_09 | 4 | 0 | 4 |
| |  |  |  |
| **Total** | **30** | **9** | **21** |
