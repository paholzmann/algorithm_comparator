

class CountingSort:
    """
    Class to sort a list of integer values using the Counting Sort algorithm.

    Counting Sort counts the occurrences of each distinct element, then
    calculates the positions of each element in the sorted output.

    Note:
        This implementation assumes the input list contains integers.

    Time Complexity:
        - O(n + k), where n is the number of elements and k is the range of input values.
    Space Complexity:
        - O(k) for the count array.

    Attributes:
        arr (list): List of integers to be sorted.
    """

    def __init__(self, arr):
        """
        Initializes the CountingSort class.

        Args:
            arr (list): List of integers.
        """
        self.arr = arr

    def sort(self):
        """
        Sorts the list in ascending order using the Counting Sort algorithm.

        Returns:
            list: Sorted list in ascending order.

        Raises:
            ValueError: If the list is empty.
        """
        if not self.arr:
            raise ValueError("Input array is empty.")

        min_value = min(self.arr)
        max_value = max(self.arr)

        count_arr = [0] * (max_value - min_value + 1)

        # Count the occurrences of each value
        for num in self.arr:
            count_arr[num - min_value] += 1

        output = []
        # Construct the sorted output list
        for index, count in enumerate(count_arr):
            value = index + min_value
            output.extend([value] * count)

        return output
