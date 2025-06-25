

class BubbleSort:
    """
    Class to sort a list of numeric values using the Bubble Sort algorithm.

    Bubble Sort repeatedly steps through the list, compares adjacent elements,
    and swaps them if they are in the wrong order. This process is repeated
    until the list is sorted.

    Time Complexity:
        - Best case: O(n) when the list is already sorted
        - Average and Worst case: O(n^2)
    Space Complexity: O(1) (in-place sorting)

    Attributes:
        arr (list): List of numbers (int or float) to be sorted.
    """

    def __init__(self, arr):
        """
        Initializes the BubbleSort class.

        Args:
            arr (list): List of numbers (int or float).
        """
        self.arr = arr

    def sort(self):
        """
        Sorts the list in ascending order using the Bubble Sort algorithm.

        Returns:
            list: Sorted list in ascending order.
        """
        n = len(self.arr)
        for i in range(n):
            swapped = False
            for j in range(n - 1 - i):  # Reduce inner loop each iteration
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
                    swapped = True
            if not swapped:  # No swaps means the list is already sorted
                break
        return self.arr
