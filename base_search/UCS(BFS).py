from priorityqueue import PriorityQueue
from graph import Graph,G2

def UCS(start, goal, came_from={}, G=G2):
    '''一致代价搜索：优先访问当前代价最低的节点'''
    '''基本BFS即每一步cost都为1的特殊UCS'''
    print(f'搜索过程为:', end='')
    frontier = PriorityQueue()
    cost_so_far = {} #目前为止的花费
    frontier.enqueue(start, 0) #start加入待查找队列
    cost_so_far[start] = 0 #cost_so_far 为某节点截至当前查找的节点的最短cost
    came_from[start] = None
    while not frontier.is_empty():
        v = frontier.dequeue()
        print(f'{v}', end='-')
        if v == goal:
            print('end')
            return goal
        else:
            for w in G.adjacentEdges(v):
                new_cost = cost_so_far[v] + G.cost(v,w) #new_cost = 前面的cost + 当前节点的cost
                if cost_so_far.get(w) == None or new_cost < cost_so_far[w]: #==None为start节点
                    cost_so_far[w] = new_cost
                    priority = new_cost
                    frontier.enqueue(w, priority)
                    came_from[w] = v #该节点为cost最小节点
    return None

def main():
    '''找到目标节点'''
    came_from = {}
    start = '1'
    goal = '12'
    found = UCS(start, goal, came_from)
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