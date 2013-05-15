from vertex import vertex as v
class graph:
    def __init__(self):
        self.lastPermVert = ''
        self.verts = []
        self.vi = 0
        self.v = 0
        return
    
    def addVertex(self, vName):
        l = len(self.verts)
        vID = l
        vObj = v(vName, vID)
        self.verts.append(vObj)
        del(vObj)
        return vID
        
    def updateVertex(self, vID, vData):
        self.verts[vID] = vData
        return
    
    def gV(self, vID):
        vtx = self.verts[vID]
        return vtx
    
    def getAllVerts(self):
        
        return self.verts
    
    def makeEdge(self, vID1, vID2, distance):
        self.verts[vID1].link(vID2, distance)
        self.verts[vID2].link(vID1, distance)
        return
    
    def listEdges(self):
        for point in range(len(self.verts)):
            l = self.verts[point].getLinks()
            for edge in range(self.verts[point].getCardinality()):
                print("Vertex", self.verts[point].getName(), "is connected to vertex",
                      self.verts[l[edge][0]].getName(), "with distance:", l[edge][1])
        return
    def listCardinality(self):
        for point in range(len(self.verts)):
            print("Edge", self.verts[point].getName(), "has a cardinality of:",self.verts[point].getCardinality())
    def getDistance(self, vID1, vID2):
        a = self.verts[vID1].getDist(vID2)
        b = self.verts[vID2].getDist(vID1)
        if a == b:
            return a
        else:
            return -1
    def vBN(self, name):
        for vert in range(len(self.verts)):
            if self.verts[vert].getName() == name:
                return vert
        return -1
    def dummyGraph(self):
        self.addVertex("A")
        self.addVertex("B")
        self.addVertex("C")
        self.addVertex("D")
        self.addVertex("E")
        self.addVertex("F")
        self.addVertex("G")
        self.addVertex("H")
        self.addVertex("I")
        self.addVertex("J")

        self.makeEdge(self.vBN('A'), self.vBN('B'), 7)
        self.makeEdge(self.vBN('A'), self.vBN('G'), 8)
        self.makeEdge(self.vBN('A'), self.vBN('H'), 5)
        self.makeEdge(self.vBN('B'), self.vBN('H'), 4)
        self.makeEdge(self.vBN('H'), self.vBN('G'), 5)
        self.makeEdge(self.vBN('G'), self.vBN('I'), 2)
        self.makeEdge(self.vBN('G'), self.vBN('F'), 7)
        self.makeEdge(self.vBN('B'), self.vBN('I'), 3)
        self.makeEdge(self.vBN('B'), self.vBN('C'), 8)
        self.makeEdge(self.vBN('C'), self.vBN('D'), 8)
        self.makeEdge(self.vBN('C'), self.vBN('I'), 5)
        self.makeEdge(self.vBN('I'), self.vBN('J'), 7)
        self.makeEdge(self.vBN('D'), self.vBN('E'), 4)
        self.makeEdge(self.vBN('D'), self.vBN('J'), 3)
        self.makeEdge(self.vBN('F'), self.vBN('E'), 6)
        self.makeEdge(self.vBN('F'), self.vBN('J'), 10)
        return
    
g = graph()
g.dummyGraph()
g.listEdges()
g.listCardinality()

