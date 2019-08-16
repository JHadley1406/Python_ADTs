

 class BinaryHeap:
    def __init__(self):
        self._heap_list = [0]
        self.current_size = 0

    def insert(self, k):
        self._heap_list.append(k)
        self.current_size += 1
        self.perc_up(self.current_size)

    def find_min(self):
        pass

    def delMin(self):
        pass

    def isEmpty(self):
        pass

    def size(self):
        pass

    def build_heap(self, list):
        pass

    def perc_up(self, i):
        while i // 2 > 0:
            if self._heap_list[i] < self._heap_list[i // 2]:
                tmp = self._heap_list[i // 2]
                self._heap_list[i // 2] = self._heap_list[i]
                self._heap_list[i] = tmp
            i = i // 2

