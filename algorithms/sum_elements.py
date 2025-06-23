
class SumElements():
    def __init__(self, arr):
        self.arr = arr
    
    def algorithm(self):
        total = 0
        for el in self.arr:
            if not isinstance(el, (int, float)):
                raise TypeError(f"Invalid type: {type(el)}")
            total += el

        return total
