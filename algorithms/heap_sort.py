

class HeapSort:
    """
    Class to sort a list of numeric values using the Heap Sort algorithm.

    Heap Sort works by building a max heap from the list, then repeatedly swapping
    the first element (maximum) with the last unsorted element, and rebuilding
    the heap for the reduced list.

    Time Complexity:
        - Best, Average, Worst: O(n log n)
    Space Complexity: O(1) (in-place sorting)

    Attributes:
        arr (list): List of numbers (int or float) to be sorted.
    """

    def __init__(self, arr):
        """
        Initializes the HeapSort class.

        Args:
            arr (list): List of numbers (int or float).
        """
        self.arr = arr

    def sort(self):
        """
        Sorts the list in ascending order using the Heap Sort algorithm.

        Returns:
            list: Sorted list in ascending order.
        """

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

        n = len(self.arr)

        # Build max heap
        for i in range(n // 2 - 1, -1, -1):
            heapify(i, n)

        # Extract elements one by one from the heap
        for i in range(n - 1, 0, -1):
            # Swap current root (largest) with the end
            self.arr[0], self.arr[i] = self.arr[i], self.arr[0]
            # Call max heapify on the reduced heap
            heapify(0, i)

        return self.arr
