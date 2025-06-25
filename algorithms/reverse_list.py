
class ReverseList():
    """
    Class to reverse the elements in a list.

    Attributes:
    arr (list): List of numbers (int or float) to be reversed.
    """
    def __init__(self, arr):
        """
        Initializes the class with a list of numbers.

        Args:
            arr (list): List of numbers (int or float).
        """
        self.arr = arr

    def algorithm(self):
        """
        Reverses the elements in the list in place.

        Returns:
            list: A list with all elements in reversed order.
        """
        n = len(self.arr)
        if n <= 1:
            return self.arr
        start = 0
        end = n - 1
        while start < end:
            self.arr[start], self.arr[end] = self.arr[end], self.arr[start]
            start += 1
            end -= 1
        return self.arr
