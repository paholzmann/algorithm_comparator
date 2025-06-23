

class MergeSort():
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        n = len(self.arr)
        if n <= 1:
            return self.arr
        
        middle = n // 2
        l_side = self.arr[:middle]
        r_side = self.arr[middle:]

        l_sorted = self.__class__(l_side).sort()
        r_sorted = self.__class__(r_side).sort()
        
        def merge(list_one, list_two):
            new_list = []
            while len(list_one) > 0 and len(list_two) > 0:
                if list_one[0] < list_two[0]:
                    new_list.append(list_one.pop(0))
                else:
                    new_list.append(list_two.pop(0))
            new_list.extend(list_one)
            new_list.extend(list_two)
            return new_list

        return merge(l_sorted, r_sorted)
