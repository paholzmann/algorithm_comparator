

class MergeSort:
    """
    Class to sort a list of numeric values using the Merge Sort algorithm.

    Merge Sort is a divide-and-conquer algorithm that:
    - Recursively splits the list into halves,
    - Sorts each half,
    - Merges the sorted halves to produce a fully sorted list.

    Time Complexity:
        - Best, Average, Worst: O(n log n)
    Space Complexity: O(n) due to auxiliary arrays during merging

    Attributes:
        arr (list): List of numbers (int or float) to be sorted.
    """

    def __init__(self, arr):
        """
        Initializes the MergeSort class.

        Args:
            arr (list): List of numbers (int or float).
        """
        self.arr = arr

    def sort(self):
        """
        Sorts the list in ascending order using Merge Sort.

        Returns:
            list: Sorted list in ascending order.
        """
        n = len(self.arr)
        if n <= 1:
            return self.arr

        middle = n // 2
        left_side = self.arr[:middle]
        right_side = self.arr[middle:]

        left_sorted = self.__class__(left_side).sort()
        right_sorted = self.__class__(right_side).sort()

        return self._merge(left_sorted, right_sorted)

    @staticmethod
    def _merge(list_one, list_two):
        """
        Merges two sorted lists into a single sorted list.

        Args:
            list_one (list): First sorted list.
            list_two (list): Second sorted list.

        Returns:
            list: Merged sorted list.
        """
        merged = []
        i, j = 0, 0
        while i < len(list_one) and j < len(list_two):
            if list_one[i] < list_two[j]:
                merged.append(list_one[i])
                i += 1
            else:
                merged.append(list_two[j])
                j += 1
        # Append remaining elements (if any)
        merged.extend(list_one[i:])
        merged.extend(list_two[j:])
        return merged
