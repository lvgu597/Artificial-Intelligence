from queue import Queue
from stack import Stack
from simplegraph import SimpleGraph,G1

def BFS(start, goal, came_from={}, G=G1):
    '''came_from: dic 该节点来自于某个节点'''
    '''BFS的队列实现'''

    print(f'搜索过程为:', end='')
    frontier = Queue()  #待搜索队列
    frontier.enqueue(start)
    came_from[start] = None
    visited_start = {} #这里visited是防止重复搜索

    last_queue = Queue()
    last_queue.enqueue(goal)
    visited_goal = {} 

    while not frontier.is_empty() and not last_queue.is_empty():
        v_start = frontier.dequeue()
        visited_start[v_start] = True #标记为搜索过
        
        v_goal = last_queue.dequeue()
        visited_goal[v_goal] = True

        print(f'{v_start}-{v_goal}', end = '-')
        if visited_start.keys() & visited_goal.keys(): #两边搜索存在交集，找到目标
            print('end')
            return goal 
        else:
            for w_start in G.adjacentEdges(v_start):
                if visited_start.get(w_start) == None: #从start开始搜索，未搜索过该节点
                    frontier.enqueue(w_start)
                    if w_start not in came_from:
                        came_from[w_start] = v_start
            for w_goal in G.adjacentEdges(v_goal):
                if visited_goal.get(w_goal) == None:
                    last_queue.enqueue(w_goal)
                    if v_goal not in came_from:
                        came_from[v_goal] = w_goal
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