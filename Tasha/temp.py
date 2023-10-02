import warnings
import numpy as np


def convTemp(x, fro='C', to='F'):
    if fro not in ['C', 'F', 'K'] or to not in ['C', 'F', 'K']:
        raise ValueError("Invalid temperature unit. Use 'C' for Celsius, 'F' for Fahrenheit, or 'K' for Kelvin.")

    if fro == to:
        warnings.warn("Your 'fro' parameter is the same as your 'to' parameter!")
        return x

    if type(x) == int or type(x) == float:
        if fro == 'C' and to == 'F':
            return 9/5 * x + 32
        elif fro == 'C' and to == 'K':
            return x + 273.15
        elif fro == 'F' and to == 'C':
            return 5/9 * (x - 32)
        elif fro == 'F' and to == 'K':
            return 5/9 * (x - 32) + 273.15
        elif fro == 'K' and to == 'C':
            return x - 273.15
        elif fro == 'K' and to == 'F':
            return 9/5 * (x - 273.15) + 32

    elif type(x) == list:
        answer_list = []
        for element in x:
            if fro == 'C' and to == 'F':
                answer = 9 / 5 * element + 32
            elif fro == 'C' and to == 'K':
                answer = element + 273.15
            elif fro == 'F' and to == 'C':
                answer = 5 / 9 * (element - 32)
            elif fro == 'F' and to == 'K':
                answer = 5 / 9 * (element - 32) + 273.15
            elif fro == 'K' and to == 'C':
                answer = element - 273.15
            elif fro == 'K' and to == 'F':
                answer = 9 / 5 * (element - 273.15) + 32

            answer_list.append(answer)
        return answer_list



# print(convTemp(0))
# print(convTemp([0, 10, 20]))
# print(convTemp(104, fro="F", to="C"))
# print(convTemp([68, -4, 59], fro="F", to="C"))
# Examples
#
assert abs(convTemp(30, to="K") - 303.15) < 1e-10
assert max(abs(np.array(convTemp([283.15, 322], fro="K")) - np.array([50, 119.93]))) < 1e-10

assert convTemp(0) == 32
assert convTemp([0, 10, 20]) == [32, 50, 68]

assert convTemp(104, fro="F", to="C") == 40
assert convTemp([68, -4, 59], fro="F", to="C") == [20, -20, 15]

assert type(convTemp([58, 104, 32], fro="F", to="C")) == list
assert len(convTemp([58, 104, 32], fro="F", to="C")) == len([58, 104, 32])

with warnings.catch_warnings(record=True) as w:
    # trigger a warning
    convTemp(58, fro="F")
    # verify the message
    assert str(w[-1].message) == "Your 'fro' parameter is the same as your 'to' parameter!"

with warnings.catch_warnings(record=True) as w:
    # Trigger a warning.
    convTemp(58, to="K", fro="K")
    # Verify the message
    assert str(w[-1].message) == "Your 'fro' parameter is the same as your 'to' parameter!"

