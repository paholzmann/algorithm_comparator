
class InsertionSort():
    def __init__(self, arr):
        self.arr = arr

    def algorithm(self):
        n = len(self.arr)
        for i in range(1, n):
            key = self.arr[i]
            j = i - 1
            while j >= 0 and self.arr[j] > key:
                self.arr[j + 1] = self.arr[j]
                j -= 1

            self.arr[j + 1] = key
        return self.arr
