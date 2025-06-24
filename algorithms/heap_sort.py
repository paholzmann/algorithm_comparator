

class HeapSort():
    def __init__(self, arr):
        self.arr = arr

    def algorithm(self):
        n = len(self.arr)
        biggest_number = self.arr.index(max(self.arr))

        def heapify(index, heap_size):
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2
            
            if left < heap_size and self.arr[left] > self.arr[largest]:
                largest = left
            if right < heap_size and self.arr[right] > self.arr[largest]:
                largest = right
            
            if largest != index:
                self.arr[index], self.arr[largest] = self.arr[largest], self.arr[index]
                heapify(largest, heap_size)

        for i in range(n // 2 - 1, -1, -1):
            heapify(i, n)

        for i in range(n - 1, 0, -1):
            self.arr[0], self.arr[i] = self.arr[i], self.arr[0]
            heapify(0, i)

            
        return self.arr
