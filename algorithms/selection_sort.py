
class SelectionSort():
    """
    Class to sort all numeric values in a list using the selection sort algorithm.

    Attributes:
        arr (list): List of numbers (int or float) to be sorted.
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
        Sorts all numbers in the list ascending order using selection sort.

        Retruns:
            list: Sorted list in ascending order
        """
        n = len(self.arr)
        if n <= 1:
            return self.arr
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if self.arr[j] < self.arr[min_index]:
                    min_index = j
            self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]
        return self.arr
