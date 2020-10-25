import heapq
'''heapq 为自内置的堆库'''

class PriorityQueue:
    '''实现简单的优先队列'''
    def __init__(self):
        self.elements = []
    
    def enqueue(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def dequeue(self):
        '''headppop 弹出当前堆中优先级最小的值'''
        return heapq.heappop(self.elements)[1]
    
    def is_empty(self):
        return self.elements == []
    
    def size(self):
        return len(self.elements)


if __name__ == "__main__":
    p = PriorityQueue()
    p.enqueue('1', 2)
    p.enqueue('2', 3)
    p.enqueue('3', 1)
    p.enqueue('4', 2)
    print(p.size())
    while not p.is_empty():
        print(p.dequeue())
