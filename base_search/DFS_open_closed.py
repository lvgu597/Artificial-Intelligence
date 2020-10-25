from stack import Stack
from graph import Graph, G2

def DFS(start, goal, came_from, G=G2):
    print(f'搜索过程为:', end='')
    open = [start] #和bfs的不同在于插入open表的位置不同
    closed = []
    came_from[start] = None
    while open:
        v = open.pop(0)
        print(f'{v}', end='-')
        if v == goal:
            print('end')
            return v
        else:
            closed.append(v)
            for w in G.adjacentEdges(v)[::-1]:
                if w not in closed and w not in open:
                    open.insert(0, w)
                    came_from[w] = v
    return  None

def main():
    '''找到目标节点'''
    came_from = {}
    start = '1'
    goal = '12'
    found = DFS(start, goal, came_from)
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
