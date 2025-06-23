

class MinMax():
    def __init__(self, arr):
        self.arr = arr

    def algorithm(self):
        n = len(self.arr)
        if n <= 1:
            return self.arr


        
        def find_min():
            min_value = self.arr[0]
            for element in self.arr:
                if element < min_value:
                    min_value = element
            return min_value

        def find_max():
            max_value = self.arr[0]
            for element in self.arr:
                if element > max_value:
                    max_value = element
            return max_value

        return find_min(), find_max()
