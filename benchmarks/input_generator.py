
import numpy as np

class InputGenerator():
    def __init__(self):
        self.short_data_length = [1, 5, 10]
        self.normal_data_length = [100, 500, 1000]
        self.long_data_length = [10000, 50000, 100000]
        self.very_long_data_length = [1000000, 5000000, 10000000]
        self.min_value = 0
        self.max_value = 10000

    def generate_random_data(self):
        data = np.random.randint(self.min_value, self.max_value, self.normal_data_length[0])
        return data

    def generate_sorted_data(self):
        data = self.generate_random_data()
        data = np.sort(data)
        return data

    def generate_reveresed_data(self):
        data = self.generate_random_data()
        data = np.sort(data)[::-1]
        return data

    def generate_duplicated_data(self):
        data = self.generate_random_data()
        data = np.repeat(data, 2)
        return data

    def generate_nearly_sorted_data(self):
        data = self.generate_sorted_data()
        num_swaps = len(data) // 5
        for _ in range(num_swaps):
            i, j = np.random.choice(len(data), 2, replace=False)
            data[i], data[j] = data[j], data[i]
        return data
