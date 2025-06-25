

class QuickSort:
    """
    Class to sort a list of numeric values using the QuickSort algorithm.

    QuickSort is a divide-and-conquer algorithm that:
    - Selects a 'pivot' element,
    - Partitions the list into elements less than, equal to, and greater than the pivot,
    - Recursively sorts the partitions,
    - Concatenates the results.

    Average Time Complexity: O(n log n)  
    Worst-case Time Complexity: O(n^2) (rare, depends on pivot selection)  
    Space Complexity: O(log n) due to recursion stack

    Attributes:
        arr (list): List of numbers (int or float) to be sorted.
    """

    def __init__(self, arr):
        """
        Initializes the QuickSort class.

        Args:
            arr (list): List of numbers (int or float).
        """
        self.arr = arr

    def sort(self):
        """
        Recursively sorts the list in ascending order using QuickSort.

        Returns:
            list: Sorted list in ascending order.
        """
        n = len(self.arr)
        if n <= 1:
            return self.arr

        pivot_index = n // 2
        pivot_value = self.arr[pivot_index]

        left_list = []
        middle_list = []
        right_list = []

        for element in self.arr:
            if element < pivot_value:
                left_list.append(element)
            elif element > pivot_value:
                right_list.append(element)
            else:
                middle_list.append(element)

        # Recursively sort left and right partitions
        return QuickSort(left_list).sort() + middle_list + QuickSort(right_list).sort()
