#! /usr/bin/env python
""" Graph Class Definition with no implementation
    to be used as a template for Graph Algorithms course """

"""This file has been modified to remove edge from graph
"""

class Graph:
    """ class initializer """

    def __init__(self, filename=None):
        # initialize to empty graph
        # Placeholder for keys to vertices
        self.V = set([])
        # number of vertices
        self.nV = 0
        # number of edges
        self.nE = 0
        # Placeholder for adjacency matrix
        self.AM = {}
        # Placeholder for adjacency list. 
        self.AL = {}
        # placeholder for weight
        self.W = {}
        if filename:
            self.readfile(filename)

    def addVertex(self, k):
        if k in self.V:
            return
        # Add an element to the vertex set
        self.AL[k] = []
        self.V.add(k)

    def addEdge(self, u, v, w=None):
        # first we check that u is a vertex
        if not u in self.V:
            ermsg = str(u) + ' not a vertex'
            raise KeyError(ermsg)
        # if v is not a vertex:
        if not v in self.V:
            ermsg = str(v) + ' not a vertex'
            raise KeyError(ermsg)
        ###This code is for adjacency list.
        if not u in self.AL:
            self.AL[u] = []
        self.AL[u].append(v)
        ## Adjust the weight
        if not w is None:
            self.W[(u, v)] = w

    def adj(self, u):
        # return an iterable of elements adjacent to u
        return self.AL[u]

    def isAdj(self, u, v):
        ## Return true if (u,v) is an edge
        return False

    # Modified part to remove and edge
    def remove(self, u, v):
        self.AL[v].remove(u)
        self.AL[u].remove(v)
        self.W.pop((u,v), None)
        self.W.pop((v,u), None)

    """ input method for files """

    def readfile(self, filename):
        ff = open(filename, 'r')
        for ll in ff.readlines():
            try:
                u = int(ll.split(':')[0].strip())
            except:
                continue
            if not u in self.V:
                self.addVertex(u)
            for vv in ll.split(':')[1].split():
                try:
                    v = int(vv)
                except:
                    uv = vv.strip('()').split(',')
                    v = int(uv[0])
                    w = float(uv[1])
                    self.addVertex(v)
                    self.addEdge(u, v, w)
                    continue
                if not v in self.V:
                    self.addVertex(v)
                self.addEdge(u, v)

    def writefile(self, filename):
        ff = open(filename, 'w')
        i = 0
        for u in self.V:
            i += 1
            ff.write(str(u))
            ff.write(": ")
            for v in self.AL[u]:
                ff.write(str(v))
                ff.write(" ")
            if (i < len(self.V)):
                ff.write('\n')


""" Testcode for when this is run as Main: """
if __name__ == "__main__":
    g = Graph('testgraph')
    print(g.V)
    print(g.AL)
    g2 = Graph('testgraph_weighted')
    print(g2.W)
    g.writefile('test_copy')
