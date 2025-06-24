

class QuickSort():
    def __init__(self, arr):
        self.arr = arr

    def algorithm(self):
        n = len(self.arr)
        if n <= 1:
            return self.arr
        pivot = n // 2

        left_list = []
        middle_list = []
        right_list = []

        for i in range(n):
            if self.arr[i] < self.arr[pivot]:
                left_list.append(self.arr[i])
            elif self.arr[i] > self.arr[pivot]:
                right_list.append(self.arr[i])
            elif self.arr[i] == self.arr[pivot]:
                middle_list.append(self.arr[i])

        return self.__class__(left_list).algorithm() + middle_list + self.__class__(right_list).algorithm()
