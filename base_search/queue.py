class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item:int) -> list:
        '''入队列，从0的位置插入'''
        self.items.insert(0,item)

    def dequeue(self) -> int:
        '''弹出最后面的元素'''
        return self.items.pop()

    def is_empty(self) -> bool:
        '''判断是否为空'''
        return self.items == []
    
    def size(self) -> int: 
        '''返回item长度'''
        return len(self.items)
    
def main():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.size())
    while not q.is_empty():
        print(q.dequeue())
    print(q.size())

if __name__ == "__main__":
    main()