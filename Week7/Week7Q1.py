class Graph(object):
    '''Class of Graph that stores a list nodes of graph and a Matrix of connections'''
    def __init__(self,value):
        N = 5
        self.node = []
        self.node.append(value)     #Add first node to graph 
        self.connections = [[0 for i in range(N)]for j in range(N)]

    def insertNode(self,item):
        '''Function that adds and creates new nodes. Send it the node value and the graph you are
        adding it to,If new graph send it None'''
        if self == None:            #Creates new graph
            self = Graph(item)
        else:
            self.node.append(item)
        return self

    def insertEdge(self, N1,N2):
        '''Function that adds a connection to the adjacency matrix in the graph.
        send it the two nodes the connection is between'''
        if (N1 in self.node) and (N2 in self.node): 
            self.connections[N1-1][N2-1] = self.connections[N1-1][N2-1] + 1
            self.connections[N2-1][N1-1] = self.connections[N2-1][N1-1] + 1

if __name__ == '__main__':
    
    g = Graph.insertNode(None,1);
    g.insertNode(2)
    g.insertNode(3)
    g.insertNode(4)
    g.insertNode(5)
    g.insertEdge(1,2)
    g.insertEdge(2,5)
    g.insertEdge(2,3)
    g.insertEdge(3,4)
    
    
    for i in range(5):
            print(g.connections[i])
