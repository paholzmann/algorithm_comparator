

class CheckPalindrome:
    """
    Class to check if a given sequence (string or number) is a palindrome.

    The palindrome check ignores punctuation and is case-insensitive.

    Attributes:
        sequence (str): The input sequence to check.
    """

    def __init__(self, sequence):
        """
        Initializes the CheckPalindrome class.

        Args:
            sequence (str or int): The sequence to check.
        """
        self.sequence = str(sequence)

    def is_palindrome(self):
        """
        Checks if the sequence is a palindrome.

        Returns:
            bool: True if the sequence is a palindrome, False otherwise.
        """
        cleaned_sequence = self.remove_punctuation().lower()
        start, end = 0, len(cleaned_sequence) - 1

        while start < end:
            if cleaned_sequence[start] != cleaned_sequence[end]:
                return False
            start += 1
            end -= 1
        return True

    def remove_punctuation(self):
        """
        Removes punctuation characters from the sequence.

        Returns:
            str: The sequence without punctuation.
        """
        punctuation = {
            '.', ',', ';', ':', '!', '?', '-', '—', '(', ')', '[', ']', '{', '}',
            '"', "'", '`', '´', '„', '“', '”', '‚', '‘', '…', '/', '\\', '@', '#',
            '$', '%', '^', '&', '*', '_', '+', '=', '<', '>', '|', '~'
        }
        return ''.join(char for char in self.sequence if char not in punctuation)
