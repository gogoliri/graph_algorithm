#! /usr/bin/env python
""" Breadth-first search example """

from graafi3 import Graph

""" Breadth-first search from s. Returns a dictionary of nodes with 
    B[u] = d, such that d is distance, None if not found. """

def BFS(g, s):
    B = {}
    B[s] = 0
    Q = [s]
    while Q:
        ## Give the invariant here:
        ##
        u = Q.pop(0)
        d = B[u]
        try:
            for v in g.adj(u):
                if not v in B:
                    B[v] = d+1
                    Q.append(v)
        except:
            pass
    
    return B

""" testcode """
if __name__ == "__main__":
    g = Graph('testgraph')
    B = BFS(g,1)
    print(B)

