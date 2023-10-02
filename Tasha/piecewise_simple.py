def pwfun(x):

    if type(x) == int or type(x) == float:
        if x < -1:
            answer = round(-2*x - 2, 2)
        elif -1 <= x <= 1:
            answer = 0
        else:
            answer = round(x**2 - 1, 2)

        if type(answer) == float:
            if answer.is_integer():
                answer = int(answer)
        return answer

    elif type(x) == list:
        answer_list = []
        for element in x:
            if element < -1:
                answer = round(-2 * element - 2, 2)
            elif -1 <= element <= 1:
                answer = 0
            else:
                answer = round(element ** 2 - 1, 2)
            if type(answer) == float:
                if answer.is_integer():
                    answer = int(answer)
            answer_list.append(answer)
        return answer_list


# Examples
print(pwfun(2))  # Example with a single value
print(pwfun([-2, 0.5, 3]))  # Example with an array
print(pwfun([-3.0, -2.5, -1, 0, 1, 2, 3.2]))  # Example with an array

# 1. inputs can be a single number ie. 4 or it can be a list ie [1,2,3,4]
# 2. apply the piecewise function to every input and round to 2 decimal places
# 3. if the answer to the piecewise function is a whole number then return without decimal point.