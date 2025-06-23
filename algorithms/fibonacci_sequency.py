
class FibonacciSequency():
    def __init__(self, length):
        self.length = length

    def algorithm(self):
        values = [0, 1]
        result = 0
        for i in range(self.length - 2):
            value = values[-1] + values[-2]
            values.append(value)
            result += value
        return result
