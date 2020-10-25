from stack import Stack
from graph import G2,Graph

def DFS(start, goal, came_from, G=G2):
    print(f'搜索过程为:', end='')
    frontier = Stack()
    frontier.push(start)  #使用栈结构存储未搜索节点
    came_from[start] = None
    visited = {} #visited 防止在搜索过程中搜索回去
    while not frontier.is_empty():
        v = frontier.pop()
        if visited.get(v) == None:
            print(f'{v}', end='-') #搜索过不会继续搜索
            if v == goal:
                print('end')
                return v
            else:
                visited[v] = True
                for w in G.adjacentEdges(v)[::-1]: #[::-1] 表示后面的元素先入栈，后搜索
                    frontier.push(w)
                    if w not in came_from:
                        came_from[w] = v
    return None

def main():
    '''找到目标节点'''
    came_from = {}
    start = '1'
    goal = '12'
    found = DFS(start, goal, came_from)
    print('start:', start)
    print('goal:', goal)
    path = [] #存储路径
    while found:
        path.append(found)
        found = came_from.get(found)
    print('-'.join(path[::-1]))

if __name__ == "__main__":
    main()
