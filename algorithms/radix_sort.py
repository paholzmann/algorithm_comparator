

class RadixSort:
    """
    Class to sort a list of non-negative integers using the radix sort algorithm.

    Radix Sort is a non-comparative sorting algorithm that processes numbers digit by digit, 
    starting from the least significant digit (LSD) to the most significant digit (MSD). 
    It uses a stable sorting method at each digit level (typically counting sort or bucket sort). 
    The key idea is that numbers are grouped into buckets based on their current digit.

    Time Complexity:
        - Best/Average/Worst: O(n * k), where n is the number of elements, and k is the number of digits.

    Limitations:
        - Only works on non-negative integers in this implementation.

    Attributes:
        arr (list): List of non-negative integers to be sorted.
    """

    def __init__(self, arr):
        """
        Initializes the RadixSort class.

        Args:
            arr (list): List of non-negative integers.

        Raises:
            ValueError: If any element is not a non-negative integer.
        """
        if not all(isinstance(x, int) and x >= 0 for x in arr):
            raise ValueError("RadixSort only supports non-negative integers.")
        self.arr = arr

    def sort(self):
        """
        Sorts the list in ascending order using radix sort.

        The algorithm works by:
        1. Finding the number with the most digits.
        2. For each digit position (units, tens, hundreds, etc.):
            - Placing each number into a bucket (0–9) based on that digit.
            - Rebuilding the list by concatenating buckets in order.

        Returns:
            list: The sorted list in ascending order.
        """
        if len(self.arr) <= 1:
            return self.arr

        max_digits = len(str(max(self.arr)))
        digit_pos = 0

        while digit_pos < max_digits:
            # Create 10 buckets for each digit (0 through 9)
            buckets = [[] for _ in range(10)]

            # Place elements in corresponding bucket
            for num in self.arr:
                digit = (num // (10 ** digit_pos)) % 10
                buckets[digit].append(num)

            # Rebuild the array by combining the buckets
            self.arr = [num for bucket in buckets for num in bucket]
            digit_pos += 1

        return self.arr
