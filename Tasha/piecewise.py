def pwfun(x):
    # Handle a single numeric value
    def compute_value(val):
        if val < -1:
            return round(-2*val - 2, 2)
        elif -1 <= val <= 1:
            return 0
        else:
            return round(val**2 - 1, 2)

    # Handle a list of values
    if isinstance(x, (list, tuple)):
        return [int(compute_value(val)) if int(compute_value(val)) == compute_value(val) else round(compute_value(val), 2) for val in x]
    elif isinstance(x, (int, float)):
        return int(compute_value(x)) if int(compute_value(x)) == compute_value(x) else round(compute_value(x), 2)
    else:
        raise ValueError("Input must be a number or a list/tuple of numbers.")

# Examples
print(pwfun(-1))  # Example with a single value
print(pwfun([-2, 0.5, 3]))  # Example with an array
print(pwfun([-3.0, -2.5, -1, 0, 1, 2, 3.2]))  # Example with an array
