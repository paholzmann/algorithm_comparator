
class RadixSort():
    def __init__(self, arr):
        self.arr = arr

    def algorithm(self):
        n = len(self.arr)
        if n <= 1:
            return self.arr
        biggest_digits = len(str(max(self.arr)))
        smallest_digits = len(str(min(self.arr)))
        digit_pos = 0
        
        while digit_pos < biggest_digits:
            buckets = [[], [], [], [], [], [], [], [], [], []]
            for num in self.arr:
                digit = (num // 10 ** digit_pos) % 10
                buckets[digit].append(num)
            new_arr = []
            for bucket in buckets:
                new_arr.extend(bucket)
            self.arr = new_arr
            digit_pos += 1
            
        return self.arr
