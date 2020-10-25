from simplegraph import SimpleGraph,G1

def BFS(start, goal, came_from={}, G=G1):
    '''came_from: dic 该节点来自于某个节点'''
    '''BFS的队列实现'''
    print(f'搜索过程为:', end='')
    open = [start]  #未访问节点列表
    closed = [] #已访问节点列表
    came_from[start] = None
    while open:
        v = open.pop(0)
        print(f'{v}', end='-')
        if v == goal:
            print(f'end')
            return v
        else:
            closed.append(v)
            for w in G.adjacentEdges(v):
                if w not in closed:
                    open.append(w)  #未搜索过的才添加进open列表
                    came_from[w] = v
    return None

def main():
    '''找到目标节点'''
    came_from = {}
    start = '1'
    goal = '5'
    found = BFS(start, goal, came_from)
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