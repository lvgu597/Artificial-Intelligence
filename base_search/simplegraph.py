class SimpleGraph:
    def __init__(self):
        self.edges = {}
    
    def adjacentEdges(self, v):
        '''获取与之相邻的边'''
        return self.edges[v]
    
G1 = SimpleGraph()
# G1.edges = {
#     '1' : ['2', '3', '4'], 
#     '2' : ['5', '6'], 
#     '3' : [], 
#     '4' : ['7', '8'], 
#     '5' : ['9', '10'], 
#     '6' : [], 
#     '7' : ['11', '12'], 
#     '8' : [], 
#     '9' : [], 
#     '10' : [], 
#     '11' : [], 
#     '12' : [] 
#     }    
G1.edges = { #邻接表的形式存储
    '1' : ['2', '3', '4'], 
    '2' : ['1', '5', '6'], 
    '3' : ['1'], 
    '4' : ['1', '7', '8'], 
    '5' : ['2', '9', '10'], 
    '6' : ['2'], 
    '7' : ['4', '11', '12'], 
    '8' : ['4'], 
    '9' : ['5'], 
    '10' : ['5'], 
    '11' : ['7'], 
    '12' : ['7'] 
    }  
