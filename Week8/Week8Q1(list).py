class Node(object):
    '''Class that contains different nodes and their key values'''
    def __init__(self,value):
        self.value = value
        self.connection = []
        self.totalWeight = None
        self.path = None
    def add_Connection(self,value):
        '''Adds a connection to the node adjacency list'''
        self.connection.append(value)

class Graph(object):
    '''Class that stores graphs full of nodes'''
    def __init__(self,value):
        self.nodes = value
        
    def insertNode(self,Node):
        '''Inserts a node from class Node and adds it to the list of nodes in the array'''
        if self == None:
            self = Graph(Node)
            
        else:
            self.nodes.append(Node)
        return self

    def insertEdge(self,n1,n2,weight):
        '''Inserts an edge between two nodes and add then to the node adjacency list'''
        if (n1 in self.nodes) and (n2 in self.nodes):
            self.nodes[self.nodes.index(n1)].add_Connection([n2,weight])
            self.nodes[self.nodes.index(n2)].add_Connection([n1,weight])

    def Dijkstra(self,start,end):
        '''Function that works out the shortest path to take in the graph'''
        CurrentN = start
        Queue = [start]
        visitedN = []
        for i in range(len(self.nodes)):
            self.nodes[i].totalWeight = 99999   #Sets total weight for all nodes to high number
        CurrentN.totalWeight = 0                #Sets the start node total weight to 0 
                
        while CurrentN != end:
            CurrentN = Queue.pop(0)
            for i in range(len(CurrentN.connection)):
                AdNode = CurrentN.connection[i] #Finds connection to a node
                if CurrentN.totalWeight + AdNode[1] < AdNode[0].totalWeight:
                    AdNode[0].totalWeight = CurrentN.totalWeight + AdNode[1]
                    AdNode[0].path = CurrentN
                    Queue.append(AdNode[0])
                    Queue.sort(key = lambda n:CurrentN.totalWeight)     #Sort the queue by the total weight of the nodes
            visitedN.append(CurrentN)

        path = []
        num = end
        
        while num != start:                     #Works out the path it took 
            path.append(num.value)
            num = num.path
        path.append(start.value)
        path.reverse()
        return path
                    



            
        
if __name__ == '__main__':
    N1 = Node(1)
    N2 = Node(2)
    N3 = Node(3)
    N4 = Node(4)
    N5 = Node(5)
    N6 = Node(6)
    N7 = Node(7)
    g = Graph([N1,N2,N3,N4,N5,N6])
    g.insertNode(N7)
    
    g.insertEdge(N1,N2,2)
    g.insertEdge(N1,N3,5)
    g.insertEdge(N2,N3,2)
    g.insertEdge(N2,N4,4)
    g.insertEdge(N3,N4,1)
    g.insertEdge(N2,N5,6)
    g.insertEdge(N3,N6,3)
    g.insertEdge(N4,N5,8)
    g.insertEdge(N4,N6,1)
    g.insertEdge(N5,N7,1)
    g.insertEdge(N6,N7,2)
    #g.insertEdge(N4,N7,1)
             
    print(g.Dijkstra(N1,N7))
    
   
