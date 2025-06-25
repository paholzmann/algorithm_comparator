

class SumElements():
    """
    Class to sum all numeric values in a list.

    Attributes:
        arr (list): List of numbers (int or float) to be summed.
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
        Calculates the sum of all numbers in the list.

        Returns:
            float: The sum of all elements

        Raises:
            TypeError: If any element is not an int or float.
        """
        total = 0 
        for el in self.arr:
            if not isinstance(el, (int, float)):
                raise TypeError(f"Invalid type: {type(el)}")
            total += el 

        return total
