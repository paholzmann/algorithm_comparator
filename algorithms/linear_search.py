

class LinearSearch:
    """
    Class to perform a linear search for an element in a list.

    Linear Search checks each element in the list sequentially until the target element is found.

    Time Complexity:
        - Best case: O(1) if the element is at the beginning
        - Worst case: O(n) if the element is not present or at the end

    Attributes:
        arr (list): List of elements to search through.
        el: Element to search for.
    """

    def __init__(self, arr, el):
        """
        Initializes the LinearSearch class.

        Args:
            arr (list): List of elements.
            el: Element to find in the list.
        """
        self.arr = arr
        self.el = el

    def search(self):
        """
        Searches for the element in the list using linear search.

        Returns:
            int: The index of the element if found, otherwise -1.
        """
        for index, element in enumerate(self.arr):
            if element == self.el:
                return index
        return -1
