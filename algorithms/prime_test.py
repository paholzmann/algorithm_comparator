

class PrimeTest():
    def __init__(self, num):
        self.num = num
        if not isinstance(self.num, (int, float)):
            raise TypeError(f"Invalid type: {type(self.num)}")
        
    def algorithm(self):
        if self.num <= 1:
            return False

        for i in range(2, int(self.num ** 0.5) + 1):
            if self.num % i == 0:
                return False
        return True
