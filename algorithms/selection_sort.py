
class SelectionSort():
    def __init__(self, arr):
        self.arr = arr

    def algorithm(self):
        n = len(self.arr)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if self.arr[j] < self.arr[min_index]:
                    min_index = j
            self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]
        return self.arr
