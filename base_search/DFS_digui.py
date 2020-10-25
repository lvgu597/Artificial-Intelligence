from graph import Graph,G2

def DFS(v, goal, came_from, G=G2):
    print(f'{v}', end='-')
    if came_from == {}:
        came_from[v] = '-1'
    if v == goal:
        print('end')
        return goal
    for w in G.adjacentEdges(v):#查找所有与该节点相连的节点
        if came_from.get(w) == None: #没搜索过
            came_from[w] = v
            result = DFS(w, goal, came_from) #递归遍历该节点
            if result == goal:
                return result
    return None

def main():
    '''找到目标节点'''
    came_from = {}
    start = '1'
    goal = '8'
    print(f'搜索过程为:', end='')
    found = DFS(start, goal, came_from)
    print('start:', start)
    print('goal:', goal)
    #print(came_from)
    path = [] #存储路径
    while found and found != '-1':
        path.append(found)
        found = came_from.get(found)
    print('-'.join(path[::-1]))

if __name__ == "__main__":
    main()
