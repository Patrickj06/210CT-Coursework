class Graph(object):
    '''Class of Graph that stores a list nodes of graph and a Matrix of connections'''
    def __init__(self,value):
        self.n = 10
        self.node = [value]     #Add first node to graph
        self.connections = [[0 for i in range(self.n)]for j in range(self.n)]
        
    def insertNode(self,item):
        '''Function that adds and creates new nodes. Send it the node value and the graph you are
        adding it to,If new graph send it None'''
        if self == None:        #Creates new graph
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

    def BFS(self,N):
        '''Function that traverses the graph using BFS,parameters are the graph its
        searchs and the starting node'''
        Queue = [N]
        visitedN = []
        while len(Queue) != 0:          
            CurrentN = Queue.pop(0)     #Pops the first thing out of the queue
            if CurrentN not in visitedN:
                visitedN.append(CurrentN)
                for i in range(len(self.node)): #Finds all connections on that node
                    if self.connections[CurrentN - 1][i] == 1:
                        Queue.append(i + 1)
                    
        return visitedN

    def DFS(self,N):
        '''Function that traverses the graph using DFS,parameters are the graph its
        searchs and the starting node'''
        Stack = [N]
        visitedN = []
        while len(Stack) != 0:
            CurrentN = Stack.pop()      #Pops the top of stack, last in the list
            if CurrentN not in visitedN:
                visitedN.append(CurrentN)            
                for i in range(len(self.node)):
                    if self.connections[CurrentN - 1][i] == 1:
                        Stack.append(i+1)

        return visitedN




if __name__ == '__main__':

    
    g = Graph.insertNode(None,1);   #Normal graph 
    g.insertNode(2)
    g.insertNode(3)
    g.insertNode(4)
    g.insertNode(5)
    g.insertEdge(1,2)
    g.insertEdge(2,5)
    g.insertEdge(2,3)
    g.insertEdge(3,4)

    g1 = Graph.insertNode(None,1);  #Binary tree
    g1.insertNode(2)
    g1.insertNode(3)
    g1.insertNode(4)
    g1.insertNode(5)
    g1.insertNode(6)
    g1.insertNode(7)
    g1.insertEdge(4,2)
    g1.insertEdge(2,1)
    g1.insertEdge(2,3)
    g1.insertEdge(4,6)
    g1.insertEdge(6,5)
    g1.insertEdge(6,7)
    #for i in range(10):
            #print(g1.connections[i])
    BFS = "BFS - ",g1.BFS(4)
    DFS = "DFS - ",g1.DFS(4)
    
    with open("text_file.txt", "w") as text_file:
        print(BFS,file = text_file)
        print(DFS,file = text_file)
