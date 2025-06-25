

class InsertionSort:
    """
    Class to sort a list of numeric values using the Insertion Sort algorithm.

    Insertion Sort builds the final sorted list one element at a time by
    comparing each new element to those already sorted and inserting it in the
    correct position.

    Time Complexity:
        - Best case: O(n) when the list is already sorted
        - Average and worst case: O(n^2)
    Space Complexity: O(1) (in-place sorting)

    Attributes:
        arr (list): List of numbers (int or float) to be sorted.
    """

    def __init__(self, arr):
        """
        Initializes the InsertionSort class.

        Args:
            arr (list): List of numbers (int or float).
        """
        self.arr = arr

    def sort(self):
        """
        Sorts the list in ascending order using the Insertion Sort algorithm.

        Returns:
            list: Sorted list in ascending order.
        """
        n = len(self.arr)
        for i in range(1, n):
            key = self.arr[i]
            j = i - 1

            # Move elements of arr[0..i-1], that are greater than key,
            # to one position ahead of their current position
            while j >= 0 and self.arr[j] > key:
                self.arr[j + 1] = self.arr[j]
                j -= 1

            self.arr[j + 1] = key

        return self.arr
