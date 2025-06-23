
class ReverseList():
    def __init__(self, arr):
        self.arr = arr

    def algorithm(self):
        n = len(self.arr)
        start = 0
        end = n - 1
        while start < end:
            self.arr[start], self.arr[end] = self.arr[end], self.arr[start]
            start += 1
            end -= 1
        return self.arr
