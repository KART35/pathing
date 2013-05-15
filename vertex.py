"""
TODO::
make link() check for edges that already exist
"""
class vertex:
    def __init__(self, vName, vID):
        self._name = vName
        self._vID = vID
        self._connects = []
        self._label = ['', -1, 'T']
        return
    def getID(self):
        return self._vID
    def getName(self):
        return self._name
    def link(self, vID, dist):
        self._connects.append([vID, dist])
        return
        
    def getDist(self, otherID):
        for i in range(len(self._connects)):
            if self._connects[i][0] == otherID:
                return self._connects[i][1]
        return -1 #not connected!
    def getCardinality(self):
        return len(self._connects)
    def getLinks(self):
        return self._connects
    
