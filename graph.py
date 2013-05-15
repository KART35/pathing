from vertex import vertex as v
class graph:
    def __init__(self):
        self.lastPermVert = ''
        self.verts = []
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
    
g = graph()
g.addVertex("A")
g.addVertex("B")
g.addVertex("C")
g.addVertex("D")
g.addVertex("E")
g.addVertex("F")
g.addVertex("G")
g.addVertex("H")
g.addVertex("I")
g.addVertex("J")

g.makeEdge(g.vBN('A'), g.vBN('B'), 7)
g.makeEdge(g.vBN('A'), g.vBN('G'), 8)
g.makeEdge(g.vBN('A'), g.vBN('H'), 5)
g.makeEdge(g.vBN('B'), g.vBN('H'), 4)
g.makeEdge(g.vBN('H'), g.vBN('G'), 5)
g.makeEdge(g.vBN('G'), g.vBN('I'), 2)
g.makeEdge(g.vBN('G'), g.vBN('F'), 7)
g.makeEdge(g.vBN('B'), g.vBN('I'), 3)
g.makeEdge(g.vBN('B'), g.vBN('C'), 8)
g.makeEdge(g.vBN('C'), g.vBN('D'), 8)
g.makeEdge(g.vBN('C'), g.vBN('I'), 5)
g.makeEdge(g.vBN('I'), g.vBN('J'), 7)
g.makeEdge(g.vBN('D'), g.vBN('E'), 4)
g.makeEdge(g.vBN('D'), g.vBN('J'), 3)
g.makeEdge(g.vBN('F'), g.vBN('E'), 6)
g.makeEdge(g.vBN('F'), g.vBN('J'), 10)

g.listEdges()
g.listCardinality()

