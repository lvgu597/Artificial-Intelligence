from stack import Stack
from graph import Graph,G2

MAX_DEPTH = 10

def IDDFS(v, goal, came_from, G=G2):
    print(f'搜索过程为:', end='')
    came_from[v] = None
    for depth in range(MAX_DEPTH+1):
        visited = {}
        found = DLS(v, goal, depth, came_from, visited, G)
        if found != None:
            print('end')
            return found
    return None
    

def DLS(v, goal, depth, came_from, visited={}, G=G2):
    visited[v] = True
    print(f'{v}', end='-')
    if depth == 0:
        if v == goal:
            return v
        else:
            return None
    elif depth > 0:
        
        for w in G.adjacentEdges(v):
            if visited.get(w) == None:
                if w not in came_from:
                    came_from[w] = v
                found = DLS(w, goal, depth-1, came_from, visited, G)  #递归实现
                if found != None:
                    return found
        return None

def main():
    '''找到目标节点'''
    came_from = {}
    start = '1'
    goal = '12'
    found = IDDFS(start, goal, came_from)
    print('start:', start)
    print('goal:', goal)
    #print(came_from)
    path = [] #存储路径
    while found :
        path.append(found)
        found = came_from.get(found)
    print('-'.join(path[::-1]))

if __name__ == "__main__":
    main()
