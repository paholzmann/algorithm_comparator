
class BubbleSort:
    def __init__(self, arr):
        self.arr = arr


    def algorithm(self):
        n = len(self.arr)
        for i in range(n):
            for j in range(n - 1):
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
        return self.arr
