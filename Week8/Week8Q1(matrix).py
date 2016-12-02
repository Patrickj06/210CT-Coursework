class Graph(object):
    
    def __init__(self,value):
        self.n = 7
        self.node = [value]
        self.connections = [[0 for i in range(self.n)]for j in range(self.n)]
        
    def insertNode(self,item):
        if self == None:
            self = Graph(item)
        else:
            self.node.append(item)
        return self

    def insertEdge(self,N1,N2,weight):
        if (N1 in self.node) and (N2 in self.node):
            self.connections[N1-1][N2-1] = weight
            self.connections[N2-1][N1-1] = weight

    def Dijkstra(self,start,end):
        CurrentN = start
        totalWeight = [0 for i in range(self.n)]
        Queue = [0]
        paths = {}
        visitedN = []
        
        for i in range(len(self.node)):
            if i == start - 1:
                totalWeight[i] = 0
            else:
                totalWeight[i] = 99999
        
        while CurrentN != end:
            
            nextN = [i for i,n in enumerate(totalWeight) if n == Queue[0]]
            for i in range(len(nextN)):
                if nextN[i] + 1 not in visitedN:
                    CurrentN = nextN[i] + 1
                    Queue.pop(0)
                    break

            for i in range(len(self.node)):
                node = self.connections[CurrentN - 1][i]
                if (node != 0) and (i + 1 not in visitedN):
                    if totalWeight[CurrentN - 1] + node < totalWeight[i]:
                        if totalWeight[i] in Queue:
                            Queue.remove(totalWeight[i])
                        totalWeight[i] = totalWeight[CurrentN - 1] + node
                        paths[i+1] = CurrentN
                        Queue.append(totalWeight[i])
                        Queue.sort()
                        
            visitedN.append(CurrentN)

        path = [end]
        number = end
        done = False
        while done == False:
            path.append(paths[number])
            number = paths[number]
            if number == start:
                done = True
        path.reverse()
        
        return path

if __name__ == '__main__':

    
    g = Graph.insertNode(None,1);
    g.insertNode(2)
    g.insertNode(3)
    g.insertNode(4)
    g.insertNode(5)
    g.insertNode(6)
    g.insertNode(7)
    g.insertEdge(1,2,2)
    g.insertEdge(1,3,5)
    g.insertEdge(2,3,2)
    g.insertEdge(2,4,4)
    g.insertEdge(3,4,1)
    g.insertEdge(2,5,6)
    g.insertEdge(3,6,3)
    g.insertEdge(4,5,8)
    g.insertEdge(4,6,1)
    g.insertEdge(5,7,1)
    g.insertEdge(6,7,2)
    #g.insertEdge(4,7,1)
    
    print(g.Dijkstra(1,7))
    #for i in range(7):
        #print(g.connections[i])
    
