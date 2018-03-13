from collections import deque

class MaxQueue:
    def __init__(self):
        self.queue = deque()
        self.deque = deque()

    def max(self):
        item = None
        if self.deque:
            item = self.deque[0]
        return item

    def enqueue(self, val):
        self.queue.append(val)
        while self.deque and self.deque[-1] < val:
            self.deque.pop()
        self.deque.append(val)
        print(self.queue)
        print(self.deque)

    def dequeue(self, val):
        if self.queue:
            queue_front = self.queue[0]
            if self.deque[0] == queue_front:
                self.deque.popleft()
            self.queue.popleft()
            print(self.queue)
            print(self.deque)
        else:
            return

if __name__ == "__main__":
    max_q = MaxQueue()
    l = [1,3,-1,-3,5,3,6,7]
    window = 3
    indx = 0

    while indx < window:
        max_q.enqueue(l[indx])
        indx +=1
    print("f %s"%max_q.max())
    start = 0
    while indx < len(l):
        max_q.dequeue(l[start])
        start += 1
        max_q.enqueue(l[indx])
        print(max_q.max())
        indx += 1


