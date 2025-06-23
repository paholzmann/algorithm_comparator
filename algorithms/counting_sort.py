

class CountingSort():
    def __init__(self, arr):
        self.arr = arr

    def algorithm(self):
        n = len(self.arr)
        min_value = min(self.arr)
        max_value = max(self.arr)
        count_arr = [0] * (max_value - min_value + 1)
        for num in self.arr:
            count_arr[num - min_value] += 1
        output = []
        for index, count in enumerate(count_arr):
            value = index + min_value
            for _ in range(count):
                output.append(value)

        return output
