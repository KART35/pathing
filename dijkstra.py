from graph import graph as gr
from time import time
from time import sleep
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
            myGraph.verts[vID].eLst[i][0].set_linestyle('-')
            
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
    #print(g.verts[vID].pid[0])
    g.verts[vID].pid[0].set_color('r')
    g.verts[vID].pid[0].set_marker('x')
    g.plt.draw()
    #print("making" , g.verts[vID].getName(), "permanant")
    g.lastPermVert = vID
    g.setVi(vID)
    
    return True

def traceBack(begID, endID, g):
    currID = endID
    endName = g.verts[endID].getName()
    reverse = [endName]
    
    while currID != begID:
        
        nextVert = g.verts[currID].getLabel()[0]
        lastID = currID
        currID = g.vBN(nextVert)
        reverse.append(nextVert)
        res = getEdge(g, lastID, currID)
        g.verts[currID].eLst[res][0].set_color('r')
        g.verts[currID].eLst[res][0].set_lw(3)
        g.plt.draw()
    print("Path: ", end = '')
    for i in range(len(reverse)):
        print(reverse[-i-1], ", ", sep = '', end ='')
    print ("length of",g.verts[endID].getLabel()[1], "units")
    return 

def getEdge(g, v1, v2):
    for i in range(len(g.verts[v1].eLst)):
        ref = g.verts[v1].eLst[i]
        for n in range(len(g.verts[v2].eLst)):
            if ref == g.verts[v2].eLst[n]:
                return n
def initGraph(g):
    g.addVertex('A', 0,0)
    g.addVertex('B', 1,1)
    g.addVertex('C', 1,3)
    g.addVertex('D', 0.75, 3.75)
    g.addVertex('E', 0, 4.25)
    g.addVertex('F', -1, 1)
    g.addVertex('G', -1, 3)
    g.addVertex('H', -0.75, 3.75)
    g.addVertex('I', 0, 1)
    g.addVertex('J', 0, 2)
    g.addVertex('K', 0.5, 2.5)
    g.addVertex('L', 0, 3)
    g.addVertex('M', -0.5, 1.5)
    g.addVertex('N', -0.5, 2.5)
    g.makeEdge(g.vBN('A'), g.vBN('B'),3)
    g.makeEdge(g.vBN('B'), g.vBN('C'),2)
    g.makeEdge(g.vBN('C'), g.vBN('D'),6)
    g.makeEdge(g.vBN('D'), g.vBN('E'),4)
    g.makeEdge(g.vBN('A'), g.vBN('I'),3)
    g.makeEdge(g.vBN('A'), g.vBN('F'),4)
    g.makeEdge(g.vBN('F'), g.vBN('I'),1)
    g.makeEdge(g.vBN('F'), g.vBN('M'),2)
    g.makeEdge(g.vBN('F'), g.vBN('G'),3)
    g.makeEdge(g.vBN('M'), g.vBN('G'),5)
    g.makeEdge(g.vBN('M'), g.vBN('J'),2)
    g.makeEdge(g.vBN('I'), g.vBN('K'),4)
    g.makeEdge(g.vBN('J'), g.vBN('B'),2)
    g.makeEdge(g.vBN('K'), g.vBN('B'),5)
    g.makeEdge(g.vBN('K'), g.vBN('C'),3)
    g.makeEdge(g.vBN('K'), g.vBN('D'),2)
    g.makeEdge(g.vBN('I'), g.vBN('J'),3)
    g.makeEdge(g.vBN('J'), g.vBN('L'),4)
    g.makeEdge(g.vBN('N'), g.vBN('L'),1)
    g.makeEdge(g.vBN('H'), g.vBN('G'),4)
    g.makeEdge(g.vBN('H'), g.vBN('E'),2)
    g.makeEdge(g.vBN('D'), g.vBN('H'),1)
    g.makeEdge(g.vBN('D'), g.vBN('L'),3)
    g.makeEdge(g.vBN('N'), g.vBN('J'),1)
    g.makeEdge(g.vBN('G'), g.vBN('N'),2)
    g.makeEdge(g.vBN('H'), g.vBN('L'),2)
    g.makeEdge(g.vBN('J'), g.vBN('K'),3)

            
def main(beg,end):
    myGraph = gr()
    #myGraph.dummyGraph()
    initGraph(myGraph)
    myGraph.verts[myGraph.vBN(beg)].pid[0].set_marker('x')
    myGraph.plt.margins(0.5)
    myGraph.setVi(myGraph.vBN(beg)) #set point A to be the starting point
    myGraph.setLabel(myGraph.vBN(beg), ['', 0, 'P']) #and set it to be permanant
    
    myGraph.plt.draw()
    myGraph.setEndpoint(myGraph.vBN(end)) # set E as the endpoint
    while myGraph.getLabel(myGraph.vBN(end))[2] != 'P': #untill E has a perm label...
        #sleep(0.25)
        if a(myGraph) or b(myGraph):
            continue
        else:
            break
    
    traceBack(myGraph.vBN(beg),myGraph.vBN(end), myGraph) #from the end, walk back to the start.
beg = 'A'
end  = 'H'

t0 = time() 
main(beg,end)
t1=time()
print(t1-t0, "seconds")
