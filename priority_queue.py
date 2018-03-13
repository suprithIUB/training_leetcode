class PriorityQueue:
    def __init__(self):
        self.array = []

    def add(self, item, priority):
        self.array.append((item, priority))
        self.heapify()

    def heapify(self):
        last_elem = self.array[-1][1] # priority
        last_elem_index = len(self.array) -1
        parent_index = last_elem_index//2
        while last_elem_index >=0 and self.array[parent_index][1] > self.array[last_elem_index]:
            left_child = self.array[parent_index]*2+1
            right_child = self.array[parent_index]*2 +2
            if self.array[left_child] < self.array[right_child]
                self.array[parent_index], self.array[left_child] = self.array[left_child],
                self.array[parent_index]
                last_elem_index = parent_index
                parent_index = parent_index//2
            else:
                self.array[parent_index], self.array[right_child] = self.array[right_child],
                self.array[parent_index]
                last_elem_index = parent_index
                parent_index = parent_index //2

    def min(self):
        if self.array:
            return self.array[-1][0]

    def delete(self):
        if self.array:
            self.array[0] = self.array[-1]
            self.array.pop()
            self.heapify()



