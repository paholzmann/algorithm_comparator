

class PrimeTest:
    """
    Class to test whether a given number is prime.

    Attributes:
        num (int): The number to test for primality.
    """

    def __init__(self, num):
        """
        Initializes the PrimeTest class.

        Args:
            num (int or float): The number to test.

        Raises:
            TypeError: If num is not an int or float.
            ValueError: If num is not an integer (no decimal part).
        """
        if not isinstance(num, (int, float)):
            raise TypeError(f"Invalid type: {type(num)}. Must be int or float.")
        if isinstance(num, float) and not num.is_integer():
            raise ValueError("Number must be an integer.")

        self.num = int(num)

    def is_prime(self):
        """
        Tests if the number is prime.

        Returns:
            bool: True if num is prime, False otherwise.
        """
        if self.num <= 1:
            return False
        if self.num <= 3:
            return True  # 2 and 3 are prime

        # Check for even number or divisible by 3
        if self.num % 2 == 0 or self.num % 3 == 0:
            return False

        # Test divisors from 5 to sqrt(num)
        i = 5
        while i * i <= self.num:
            if self.num % i == 0 or self.num % (i + 2) == 0:
                return False
            i += 6

        return True
