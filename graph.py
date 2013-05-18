from vertex import vertex as v
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import time

class graph:
    def __init__(self):
        self.lastPermVert = 0
        self.verts = []
        self.vi = 0
        self.v = 0
        self.endpoint = -1
        self.plt = plt
        plt.ion()
        return
    
    def addVertex(self, vName, x=0, y=0 ):
        l = len(self.verts)
        vID = l
        vObj = v(vName, vID)
        self.verts.append(vObj)
        self.verts[vID].setXY(x,y)
        self.verts[vID].pid = self.addPoint(x,y)
        plt.annotate(self.verts[vID].getName(),(y+0.05,x+0.05))
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
        plt.ion()
        self.verts[vID1].link(vID2, distance)
        self.verts[vID2].link(vID1, distance)
        hl = plt.plot([self.verts[vID1].getXY()[1],self.verts[vID2].getXY()[1]],
                      [self.verts[vID1].getXY()[0], self.verts[vID2].getXY()[0]],
                      'k-')
        plt.draw()
        #print(self.verts[vID1].getXY()[1],self.verts[vID1].getXY()[0],'->',self.verts[vID2].getXY()[1],self.verts[vID2].getXY()[0])
        return hl
    
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

    def getLabel(self, vID):
        return self.verts[vID].getLabel()

    def setLabel(self, vID, labelDat):
        if self.verts[vID].updateLabel(labelDat) == 0:
            self.lastPermVert = vID
        return

    def getSmallest(self):
        #get temporary labels...
        smallest = 1000000000000000
        smallestID = -1
        for v in range(len(self.verts)):
            if self.verts[v].getLabel()[2] == 'T':
                size = self.verts[v].getLabel()[1]
                if size < smallest:
                    smallest = size
                    smallestID = v
        return smallestID

    def getRecentPerm(self):
        return self.lastPermVert

    def setVi(self, vID):
        self.vi = vID
        return

    def setEndpoint(self, vID):
        self.endpoint = vID
        return
    def update_line(hl, new_data):
        hl.set_xdata(np.append(hl.get_xdata(), new_data[1]))
        hl.set_ydata(np.append(hl.get_ydata(), new_data[0]))
        plt.draw()
        return
    
    def addPoint(self, x, y):
        hl = plt.plot(y,x, 'ko')
        return hl
    
    def dummyGraph(self):
        
        self.addVertex("A",0,-1)
        self.addVertex("B",1,0.5)
        self.addVertex("C",1.5,1.5)
        self.addVertex("D",1.5,3)
        self.addVertex("E",1,4)
        self.addVertex("F",0,3)
        self.addVertex("G",0,1)
        self.addVertex("H",0.5,0.5)
        self.addVertex("I",1,1.5)
        self.addVertex("J",1,3)
        

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
    


