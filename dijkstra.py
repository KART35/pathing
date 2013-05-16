from graph import graph as gr
from time import time
def test():
    
    g = gr()
    g.dummyGraph()
    g.listEdges()
    g.listCardinality()
    return
def a(myGraph):
    changed = False
    vID = myGraph.getRecentPerm()
    links = myGraph.verts[vID].getLinks()
    #print (links)
    #[[vID, D], [vID, D], [vID, D]]
    for i in range(len(links)):
        thisVID = links[i][0]
        if myGraph.verts[thisVID].getLabel()[2] == 'T': #if label is temporary
            name = myGraph.verts[thisVID].getName()
            #print("Vertex", name, "is temporary")
            tDist = myGraph.verts[thisVID].getLabel()[1]
            sDist = myGraph.verts[vID].getLabel()[1]
            edgeLen = myGraph.verts[vID].getDist(thisVID)
            evalD = sDist + edgeLen
            if evalD < tDist:
                changed = True
                #print("updating vertex", name, evalD)
                L = myGraph.verts[thisVID].getLabel()
                L[1] = evalD
                L[0] = myGraph.verts[vID].getName()
    return changed

def b(g):
    vID = g.getSmallest()
    if vID == -1:
        return False
    l = g.verts[vID].getLabel()
    l[2] = 'P'
    #print("making" , g.verts[vID].getName(), "permanant")
    g.lastPermVert = g.vi
    g.setVi(g.vi +1)
    
    return True

def traceBack(begID, endID, g):
    currID = endID
    endName = g.verts[endID].getName()
    reverse = [endName]
    
    while currID != begID:
        nextVert = g.verts[currID].getLabel()[0]
        reverse.append(nextVert)
        currID = g.vBN(nextVert)
    print("Path: ", end = '')
    for i in range(len(reverse)):
        print(reverse[-i-1], ", ", sep = '', end ='')
    print ("length of",g.verts[endID].getLabel()[1], "units")
    return 

def main():
    myGraph = gr()
    myGraph.dummyGraph()
    myGraph.setVi(myGraph.vBN('A')) #set point A to be the starting point
    myGraph.setLabel(myGraph.vBN('A'), ['', 0, 'P']) #and set it to be permanant
    myGraph.setEndpoint(myGraph.vBN('E')) # set E as the endpoint
    while myGraph.getLabel(myGraph.vBN('E'))[2] != 'P': #untill E has a perm label...
        #print("")
        if a(myGraph) or b(myGraph):
            continue
        else:
            break
    
    traceBack(myGraph.vBN('A'),myGraph.vBN('E'), myGraph) #from the end, walk back to the start.
t0 = time() 
main()
t1=time()
print(t1-t0)