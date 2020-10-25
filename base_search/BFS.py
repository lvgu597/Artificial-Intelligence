from queue import Queue
from stack import Stack
from simplegraph import SimpleGraph,G1
from graph import G2,Graph

def BFS(start, goal, came_from={}, G=G2):
    '''came_from: dic 该节点来自于某个节点'''
    '''BFS的队列实现'''

    print(f'搜索过程为:', end='')
    frontier = Queue()  #待搜索队列
    frontier.enqueue(start)
    came_from[start] = None
    visited = {} #这里visited是防止重复搜索
    while not frontier.is_empty():
        v = frontier.dequeue()
        if visited.get(v) == None: #未搜索过
            print(f'{v}', end='-')
            if v == goal:
                print('end')
                return v
            else:
                visited[v] = True #标记为搜索过
                for w in G.adjacentEdges(v):
                    frontier.enqueue(w) #将所有v的子节点加入待搜索列表
                    if w not in came_from:
                        came_from[w] = v
    return None

def main():
    '''找到目标节点'''
    came_from = {}
    start = '1'
    goal = '12'
    found = BFS(start, goal, came_from, G1)
    print('start:', start)
    print('goal:', goal)
    #print(came_from)
    path = [] #存储路径
    while found:
        path.append(found)
        found = came_from.get(found)
    print('-'.join(path[::-1]))

if __name__ == "__main__":
    main()