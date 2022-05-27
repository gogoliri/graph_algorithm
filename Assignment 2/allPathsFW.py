import numpy as np
import graafi3 as graph

# Define the infinity quantity
inf = float("inf")

# Floyd Warshall algorithm
# The code assume that node are numbered from 1 to n
def FW(g):
    """The graph calculate minimal length with traditional Floyd Warshall

    :param g: a weighted graph
    :return: distance matrix d and parent matrix p
    """
    n = len(g.V) # Number of node
    # Distance matrix
    d = [[inf for i in range(n)] for j in range(n)]
    # Parent matrix of a node in a route
    p = [[inf for i in range(n)] for j in range(n)]

    # Initizalize distance matrix
    # 0 on diagonal
    # infinity otherwise
    for u in g.V:
        for v in g.V:
            if u == v:
                d[u - 1][v - 1] = 0

    # at stage 0, if 2 nodes are connected
    # the minimal path weight is their edge weight
    for u in g.V:
        for v in g.adj(u):
            d[u - 1][v - 1] = g.W[(u, v)]
            # Modified path, the parent of the end node is the starting node in an edge
            p[u - 1][v - 1] = u

    # Floyd Warshall algorithm
    for s in g.V:
        for u in g.V:
            for v in g.V:
                if d[u - 1][v - 1] > d[u - 1][s - 1] + d[s - 1][v - 1]:
                    d[u - 1][v - 1] = d[u - 1][s - 1] + d[s - 1][v - 1]
                    p[u - 1][v - 1] = p[s - 1][v - 1]

    return d, p

# Modified FW
def allPathsFW(g):
    """This function calculate minimal path if there is one

    :param g: A weighted graph
    :return: the matrix path PATH
    """
    # Run the traditional FW first
    [d, p] = FW(g)
    n = len(g.V)
    # Initialize Path matrix
    PATH = [[[] for i in range(n)] for j in range(n)]

    # A boolen matrix whether there is a minimal path for route of (i, j)
    ispath = [[True for i in range(n)] for j in range(n)]

    # Test the 3 conditions of existence of minimal path
    # Write true or false to ispath accordingly if there is minimal path or not
    for i in g.V:
        for j in g.V:
            # Condition 1
            if i == j:
                if d[i - 1][j - 1] < 0:
                    ispath[i - 1][j - 1] = False
            # Condition 2
            if d[i - 1][j - 1] == inf:
                ispath[i - 1][j - 1] = False
            # Condition 3
            for k in g.V:
                if d[i - 1][j - 1] != inf and d[k - 1][k - 1] < 0 \
                        and d[i - 1][k - 1] != inf and d[k - 1][j - 1] != inf:
                    ispath[i - 1][j - 1] = False
    # Start to fill the path matrix
    for u in g.V:
        for v in g.V:
            # If there is a path, reverse search to add the parent
            # The idea is from lecture slide
            if ispath[u - 1][v - 1]:
                x = v
                # First node of path
                path = [v]
                # back search until we find u ( starting node)
                while x != u:
                    x = p[u - 1][x - 1]
                    path.insert(0, x)
                # Insert to path matrix
                PATH[u - 1][v - 1] = path
    # Return the matrix path
    return PATH


if __name__ == "__main__":
    g = graph.Graph("G12PythonFW.txt")
    PATH = allPathsFW(g)

    # Print the Path matrix in a pretty way
    # List of rows
    s = [[str(e) for e in row] for row in PATH]
    # Calculate the space
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    # Form a table for print
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))
