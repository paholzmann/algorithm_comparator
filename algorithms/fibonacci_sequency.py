

class FibonacciSequence:
    """
    Class to generate a Fibonacci sequence of a given length and calculate the sum
    of all Fibonacci numbers in the sequence (excluding the first two by your logic).

    Attributes:
        length (int): The number of Fibonacci numbers to generate.
    """

    def __init__(self, length):
        """
        Initializes the FibonacciSequence class.

        Args:
            length (int): The length of the Fibonacci sequence to generate.
        """
        if length < 1:
            raise ValueError("Length must be at least 1.")
        self.length = length

    def sum_fibonacci(self):
        """
        Generates the Fibonacci sequence up to the specified length and returns
        the sum of all Fibonacci numbers in the sequence.

        Returns:
            int: Sum of the Fibonacci numbers in the sequence.
        """
        if self.length == 1:
            return 0
        elif self.length == 2:
            return 1  # sum of [0,1]

        values = [0, 1]
        total_sum = 1  # sum of first two Fibonacci numbers

        for _ in range(self.length - 2):
            next_value = values[-1] + values[-2]
            values.append(next_value)
            total_sum += next_value

        return total_sum
