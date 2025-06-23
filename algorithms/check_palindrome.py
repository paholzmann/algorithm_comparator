

class CheckPalindrome():
    def __init__(self, sequence):
        self.sequence = str(sequence)

    def algorithm(self):
        palindrome = None
        new_sequence = self.remove_punctuation().lower()
        sequence_list = list(new_sequence)
        start = 0
        end = len(sequence_list) - 1
        
        while start < end:
            if sequence_list[start] != sequence_list[end]:
                return False
            start += 1
            end -= 1
        return True
            
    def remove_punctuation(self):
        new_sequence = ""
        punctuation = punctuation = [
            '.', ',', ';', ':', '!', '?', '-', '—', '(', ')', '[', ']', '{', '}',
            '"', "'", '`', '´', '„', '“', '”', '‚', '‘', '…', '/', '\\', '@', '#',
            '$', '%', '^', '&', '*', '_', '+', '=', '<', '>', '|', '~'
        ]
        for char in self.sequence:
            if char not in punctuation:
                new_sequence += char
        return new_sequence
