import numbers


def ADD(a, b):
    """
    Adds two numbers together.

    Params:
    a, b: The numbers you want to add.

    Returns:
    The sum of a and b.
    """
    if isinstance(a, numbers.Number) and isinstance(b, numbers.Number):
        return a + b
    raise ValueError("You can only add numbers")


def SUB(a, b):
    """
    Subtracts b from a.

    Params:
    a: The number you're subtracting from.
    b: The number to subtract.

    Returns:
    The result of a - b.
    """
    if isinstance(a, numbers.Number) and isinstance(b, numbers.Number):
        return a - b
    raise ValueError("You can only subtract numbers")


def MULTIPLY(a, b):
    """
    Multiplies two numbers.

    Params:
    a, b: The numbers you want to multiply.

    Returns:
    The product of a and b.
    """
    if isinstance(a, numbers.Number) and isinstance(b, numbers.Number):
        return a * b
    raise ValueError("You can only multiply numbers")


def DIVIDE(a, b):
    """
    Divides a by b.

    Params:
    a: The number to divide.
    b: The number to divide by.

    Returns:
    The result of a / b.
    """
    if isinstance(a, numbers.Number) and isinstance(b, numbers.Number):
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return a / b
    raise ValueError("You can only divide numbers")


def POWER(a, b):
    """
    Raises a to the power of b.

    Params:
    a: The base number.
    b: The exponent.

    Returns:
    The result of a ** b.
    """
    if isinstance(a, numbers.Number) and isinstance(b, numbers.Number):
        return a ** b
    raise ValueError("You can only power between two numbers")


def GREATER_THAN(a, b):
    """
    Checks if a is greater than b.

    Params:
    a, b: The numbers you want to compare.

    Returns:
    True if a > b, otherwise False.
    """
    if isinstance(a, numbers.Number) and isinstance(b, numbers.Number):
        return a > b
    raise ValueError("You can only compare numbers")


def SMALLER_THAN(a, b):
    """
    Checks if a is smaller than b.

    Params:
    a, b: The numbers you want to compare.

    Returns:
    True if a < b, otherwise False.
    """
    if isinstance(a, numbers.Number) and isinstance(b, numbers.Number):
        return a < b
    raise ValueError("You can only compare numbers")


def EQUALS(a, b):
    """
    Checks if a is equal to b.

    Params:
    a, b: The values you want to compare.

    Returns:
    True if a == b, otherwise False.
    """
    try:
        return a == b
    except TypeError:
        raise ValueError("Values a and b cannot be compared.")


def NOT_EQUALS(a, b):
    """
    Checks if a is not equal to b.

    Params:
    a, b: The values you want to compare.

    Returns:
    True if a != b, otherwise False.
    """
    try:
        return a != b
    except TypeError:
        raise ValueError("Values a and b cannot be compared.")


def CALC_SQUARE_ROOT(a):
    """
    Calculates the square root of a.

    Params:
    a: The number you want the square root of.

    Returns:
    The square root of a.
    """
    return a ** 0.5


def CALC_MAX(a, b):
    """
    Returns the maximum of a and b.

    Params:
    a, b: The numbers you want to compare.

    Returns:
    The larger of a and b.
    """
    if a > b:
        return a
    return b


def CALC_MIN(a, b):
    """
    Returns the minimum of a and b.

    Params:
    a, b: The numbers you want to compare.

    Returns:
    The smaller of a and b.
    """
    if a < b:
        return a
    return b


def ASSIGN(name, value):
    """
    Creates an assignment statement.

    Params:
    name: The variable name as a string.
    value: The value to assign.

    Returns:
    A string like "name = value".
    """
    return f"{name} = {value}"


def AND(a, b):
    """
    Performs logical AND between two booleans.

    Params:
    a, b: The boolean values you want to 'and' together.

    Returns:
    The result of a and b.
    """
    if isinstance(a, bool) and isinstance(b, bool):
        return a and b
    raise ValueError("You can only perform 'and' on boolean values")


def OR(a, b):
    """
    Performs logical OR between two booleans.

    Params:
    a, b: The boolean values you want to 'or' together.

    Returns:
    The result of a or b.
    """
    if isinstance(a, bool) and isinstance(b, bool):
        return a or b
    raise ValueError("You can only perform 'or' on boolean values")
