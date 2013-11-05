"""
TODO::
make link() check for edges that already exist
"""
class vertex:
    def __init__(self, vName, vID):
        self._name = vName
        self._vID = vID
        self.xy = [0,0]
        self.connects = []
        self._label = ['', 100000000000000, 'T']
        self.pid = None
        self.eLst = []
        return
    def getID(self):
        return self._vID
    def setXY(self, x, y):
        self.xy[0] = x
        self.xy[1] = y

    def getXY(self):
        return self.xy
    
    def getName(self):
        return self._name
    
    def link(self, vID, dist):
        self.connects.append([vID, dist])
        return
        
    def getDist(self, otherID):
        for i in range(len(self.connects)):
            if self.connects[i][0] == otherID:
                return self.connects[i][1]
        return -1 #not connected!
    
    def getCardinality(self):
        return len(self.connects)
    
    def getLinks(self):
        return self.connects
    
    def getLabel(self):
        return self._label

    def isPerm(self):
        if self._label[2] == 'P':
            return True
        else:
            return False
        return -1
    
    def updateLabel(self, label):
        if self._label[2] !='P':
            self._label = label
            if label[2] == 'P':
                return 0
            return True
        else:
            return False
        return -1
    
    
    
