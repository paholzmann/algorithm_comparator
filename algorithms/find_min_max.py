

class MinMax:
    """
    Class to find the minimum and maximum values in a list of numbers.

    Attributes:
        arr (list): List of numbers (int or float).
    """

    def __init__(self, arr):
        """
        Initializes the MinMax class.

        Args:
            arr (list): List of numbers (int or float).
        """
        self.arr = arr

    def find_min_max(self):
        """
        Finds the minimum and maximum values in the list.

        Returns:
            tuple: A tuple containing (min_value, max_value).

        Raises:
            ValueError: If the list is empty.
        """
        if not self.arr:
            raise ValueError("Cannot find min and max of an empty list.")

        min_value = self.arr[0]
        max_value = self.arr[0]

        for element in self.arr:
            if element < min_value:
                min_value = element
            elif element > max_value:
                max_value = element

        return min_value, max_value
