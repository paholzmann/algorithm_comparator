

class LinearSearch():
    def __init__(self, arr, el):
        self.arr = arr
        self.el = el

    def algorithm(self):
        for index, element in enumerate(self.arr):
            if element == self.el:
                return index
        return -1
