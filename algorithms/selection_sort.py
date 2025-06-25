

class SelectionSort:
    """
    Class to sort a list of numeric values using the Selection Sort algorithm.

    Selection Sort is a comparison-based sorting algorithm. It divides the list into a 
    sorted and an unsorted part. It repeatedly selects the smallest element from the 
    unsorted portion and moves it to the sorted portion.

    Time Complexity:
        - Best, Average, Worst: O(n^2)
    Space Complexity: O(1) (in-place)

    Attributes:
        arr (list): List of numbers (int or float) to be sorted.
    """

    def __init__(self, arr):
        """
        Initializes the SelectionSort class.

        Args:
            arr (list): List of numbers (int or float).
        """
        self.arr = arr

    def sort(self):
        """
        Sorts the list in ascending order using the Selection Sort algorithm.

        Returns:
            list: Sorted list in ascending order.
        """
        n = len(self.arr)
        if n <= 1:
            return self.arr

        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if self.arr[j] < self.arr[min_index]:
                    min_index = j
            # Swap the found minimum with the first unsorted element
            self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]

        return self.arr
