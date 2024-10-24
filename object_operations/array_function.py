class MyArray:
    """
    A simple class to manage a dynamic array with basic operations.
    """

    def __init__(self, *args):
        """
        Initializes the MyArray instance with any number of initial elements.

        Parameters:
        *args: Variable length argument list of initial elements to include in the array.
        """
        self.array = []
        for item in args:
            self.array.append(item)

    def ADD_ITEM(self, i):
        """
        Adds an item to the end of the array.

        Parameters:
        i: The item to be added to the array.
        """
        self.array.append(i)

    def LENGTH(self):
        """
        Returns the length of the array.

        Returns:
        int: The number of elements in the array.
        """
        count = 0
        for item in self.array:
            count += 1
        return count

    def REMOVE_ITEM(self, i):
        """
        Removes the item at the specified index from the array.

        Parameters:
        i: The index of the item to be removed.

        Raises:
        ValueError: If the index is out of range.
        """
        if 0 <= i < self.LENGTH():
            self.array = self.array[:i] + self.array[i + 1:]
        else:
            raise ValueError(f"Index {i} is out of range.")

    def GET_ITEM(self, i):
        """
        Retrieves the item at the specified index from the array.

        Parameters:
        i: The index of the item to retrieve.

        Returns:
        The item at the specified index.

        Raises:
        ValueError: If the index is out of range.
        """
        if 0 <= i < self.LENGTH():
            return self.array[i]
        else:
            raise ValueError(f"Index {i} is out of range.")

    def PRINT_ARRAY(self):
        """
        Returns a string representation of the array.

        Returns:
        str: The string representation of the array.
        """
        return str(self.array)
