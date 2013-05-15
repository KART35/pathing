from vertex import vertex as v
class graph:
    
    verts = []
    def __init__(self):
        return
    
    def addVertex(self, vName):
        l = len(self.verts)
        vID = l
        vObj = v(vName, vID)
        self.verts.append(vObj)
        del(vObj)
        #print (vName, vID)
        #print (self.verts[vID].getName(), vID)
        return vID
        
    def updateVertex(self, vID, vData):
        self.verts[vID] = vData
        return
    
    def getVertex(self, vID):
        vtx = self.verts[vID]
        #print(vtx.getName(), "vtx")
        return vtx
    
    def getAllVerts(self):
        
        return self.verts
    
    def makeEdge(self, vID1, vID2, distance):
        self.verts[vID1].link(vID2, distance)
        self.verts[vID2].link(vID1, distance)
        return
    def listEdges(self):
        for point in range(len(g.verts)):
            l = g.verts[point].getLinks()
            for edge in range(g.verts[point].getCardinality()):
                print("Vertex", g.verts[point].getName(), "is connected to vertex", g.verts[l[edge][0]].getName(),
                      "with distance:", l[edge][1])


    
g = graph()
g.addVertex("A")
g.addVertex("B")
g.addVertex("C")

g.makeEdge(0, 1, 10)
#print("-",0,1, g.verts[0].getLinks(), g.verts[1].getLinks())
g.makeEdge(0, 2, 20)
#print("-",0,2, g.verts[0].getLinks(), g.verts[2].getLinks())
g.makeEdge(1, 2, 30)
g.listEdges()


