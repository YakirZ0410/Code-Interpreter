import string


class MyString:
    """
    A simple string manipulation class.
    """

    def __init__(self, string_=""):
        """
        Initializes the MyString object with a string.

        Params:
        string_: The initial string value (default is an empty string).
        """
        self.string_ = string_

    def REPLACE_STRING(self, old: str, new: str):
        """
        Replaces occurrences of 'old' with 'new' in the string.

        Params:
        old: The substring to be replaced.
        new: The substring to replace with.

        Returns:
        The modified string with 'old' replaced by 'new'.
        """
        if not self.string_.__contains__(old):
            return self.string_
        result = []
        i = 0
        while i < len(self.string_):
            if self.string_[i:i + len(old)] == old:
                result.append(new)
                i += len(old)
            else:
                result.append(self.string_[i])
                i += 1
        self.string_ = ''.join(result)
        return self.string_

    def CHECK_IF_UPPER_CASE(self):
        """
        Checks if the string is entirely in uppercase.

        Returns:
        True if the string is uppercase, False otherwise.
        """
        for char in self.string_:
            if char in string.digits or char in string.punctuation:
                continue
            if 'a' <= char <= 'z':
                return False
        return True

    def CHECK_IF_LOWER_CASE(self):
        """
        Checks if the string is entirely in lowercase.

        Returns:
        True if the string is lowercase, False otherwise.
        """
        for char in self.string_:
            if char in string.digits or char in string.punctuation:
                continue
            if 'A' <= char <= 'Z':
                return False
        return True

    def CONCATE_STRINGS(self, str2):
        """
        Concatenates another string to the current string.

        Params:
        str2: The string to be concatenated.
        """
        self.string_ = self.string_ + str2

    def PRINT_STRING(self):
        """
        Prints the current string.
        """
        print(self.string_)

    def __copy__(self):
        """
        Creates a copy of the current MyString object.

        Returns:
        A new MyString object with the same string.
        """
        return MyString(self.string_)

    def __repr__(self):
        """
        Returns a string representation of the MyString object.

        Returns:
        A string wrapped in double quotes.
        """
        return f'"{self.string_}"'
