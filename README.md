**** Shmyton Language Manual ***


Keywords:
    IF: Used for making decisions in your code. It runs code based on whether a condition is true or false.
    ELSE: Follows an IF statement and runs code if the IF condition is false.
    LOOP: Used to repeat code. You can use while or for loops to run code multiple times.
    FINISH: Stops a loop from running before it naturally finishes.
    DATA_STRUCTURE: Lets you create and work with data structures like arrays or strings.


Operators:
    OP: Includes arithmetic operators (+, -, *, /), logical operators (&&, ||), and comparison operators (==, !=, <, >).


Symbols:
    POINT: The dot (.), used for calling methods or accessing properties.
    COMMA: The comma (,), used to separate items, like in lists or function arguments.
    END: The backtick (`), marks the end of a code block or statement.
    POUND: The hash (#), used to indicate the end of a statement or block.


Data Types:
    DIGIT: Represents numbers in your code.
    BOOL: Refers to boolean values: True and False.
    LETTER: Used for string literals, which are enclosed in double quotes.


Identifiers:
    ID: Names you give to variables, functions, or other custom elements in your code.


Functions:
    ADD(a, b): Adds a and b together and returns the result. If either isn't a number, it raises a ValueError.
    SUB(a, b): Subtracts b from a and returns the result. Raises ValueError if either isn't a number.
    MULTIPLY(a, b): Multiplies a and b and returns the product. Raises ValueError if either isn't a number.
    DIVIDE(a, b): Divides a by b and returns the result. Raises a ZeroDivisionError if b is zero, and a ValueError if either isn't a number.
    POWER(a, b): Raises a to the power of b. Returns the result. Raises ValueError if either isn't a number.

    GREATER_THAN(a, b): Checks if a is greater than b. Returns True if it is; otherwise, False. Raises ValueError if either isn't a number.
    SMALLER_THAN(a, b): Checks if a is smaller than b. Returns True if it is; otherwise, False. Raises ValueError if either isn't a number.
    EQUALS(a, b): Checks if a is equal to b. Returns True if they are equal; otherwise, False. Raises ValueError if a and b can't be compared.
    NOT_EQUALS(a, b): Checks if a is not equal to b. Returns True if they are not equal; otherwise, False. Raises ValueError if a and b can't be compared.

    CALC_SQUARE_ROOT(a): Calculates and returns the square root of a.
    CALC_MAX(a, b): Returns the maximum of a and b. Gives the larger value.
    CALC_MIN(a, b): Returns the minimum of a and b. Gives the smaller value.

    ASSIGN(name, value): Creates an assignment statement like name = value. Returns this string.

    AND(a, b): Performs a logical AND on a and b (both boolean). Returns the result. Raises ValueError if either isn't a boolean.
    OR(a, b): Performs a logical OR on a and b (both boolean). Returns the result. Raises ValueError if either isn't a boolean.


Array Functions - MyArray Class:
    __init__(*args): Sets up the array with any initial elements you provide.
    ADD_ITEM(i): Adds an item i to the end of the array.
    LENGTH(): Returns the number of elements in the array.
    REMOVE_ITEM(i): Removes the item at index i. Raises ValueError if i is out of range.
    GET_ITEM(i): Gets the item at index i. Raises ValueError if i is out of range.
    PRINT_ARRAY(): Returns a string that shows the contents of the array.


String Functions - MyString Class:
    __init__(string_=""): Creates a MyString object with the string you provide (or an empty string by default).
    REPLACE_STRING(old, new): Replaces every occurrence of old with new in the string. Returns the updated string.
    CHECK_IF_UPPER_CASE(): Checks if the entire string is in uppercase. Returns True if it is; otherwise, False.
    CHECK_IF_LOWER_CASE(): Checks if the entire string is in lowercase. Returns True if it is; otherwise, False.
    CONCATE_STRINGS(str2): Adds str2 to the end of the current string.
    PRINT_STRING(): Prints the current string to the console.
    __copy__(): Makes a copy of the MyString object. Returns a new MyString object with the same string.
    __repr__(): Returns a string representation of the MyString object, enclosed in double quotes.
