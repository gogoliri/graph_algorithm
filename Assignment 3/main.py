import graafi3 as graph
import operator

# Initialize parameters
t = 0
p = {}
d = {}
color = {}

# vertex to start the search
vertex_to_start_search = 1

# DFS algorithm
def DFS(g, s):
    """Find 1 cycle in the graph by DFS
    This function call the first step of a recursive algorithm

    :param g: The target graph to perform DFS
    :param s: The initial vertex s to start DFS
    :return: An edge in a cycle
    """
    # Use the global variables
    global color
    global p
    global d
    color = {u: "white" for u in g.V}
    p = {u: None for u in g.V}
    d = {u: -1 for u in g.V}
    # Call the DFScycle algorithm on s
    e = DFScycle(g, s)
    return e


def DFScycle(g, u):
    """Recursive function to find cycle in a graph
    # This is just the DFS modified a small part

    :param g: Graph to find the cycle
    :param u: Initial vertex
    :return: return the edge of and cycle if there is one cycle and None if there is no cycle
    """
    # Use the global variables
    global t
    global color
    global p
    global d
    t += 1
    color[u] = "gray"
    d[u] = t
    # Check vertex adjacent to u
    for v in g.adj(u):
        # If v is not yet discovered
        # Perform DFS on v
        if color[v] == "white":
            p[v] = u
            e = DFScycle(g, v)
            if len(e) != 0:
                return e
        # Modified part
        # If v is discovered,
        # But v is not the parent of u
        # Then v is from a different branch of the tree
        # Indicating a cycle
        # Return edge (v,u) of the cycle
        elif color[v] == "gray" and p[u] != v:
            e = (v, u)
            return e
    color[u] = "black"
    # If there is no cycle, return nothing
    return ()


def MSTCYCLE(g):
    """Find cycles in a graph and remove largest vertex
    continue until there is no cycle

    :param g: Input graph
    :return: MST, list of cycles and removed edge in each cycle
    """
    # Initialize MST
    MST = g
    # Find an edge of the first cycle
    e = DFS(MST, vertex_to_start_search)
    # List of cycles
    list_of_cycles = []
    # The edge to be remove from edge cycles
    edge_to_be_removed = []

    # Perform to find cycle
    # While there is a cycle
    while len(e) > 0:
        # Return 2 vertex v and u
        [v, u] = e
        # weight of (v,u)
        w = g.W[e]
        # Initialize list of node in the current cycle
        list_of_node_in_cycle = [v, u]

        # edges in cycle and their weights
        edges_in_cycle_dict = {e: w}

        # Starting from u, back to p[u]
        # until we reach v
        # Add edges to a dictionary along with their weights
        while p[u] != v:
            # The current edge
            edge_in_cycle = (u, p[u])
            # and its weight
            w_of_edge = g.W[edge_in_cycle]
            # Add them to the edges in cycle dict
            edges_in_cycle_dict[edge_in_cycle] = w_of_edge
            # Add p[u] to the list of node
            list_of_node_in_cycle.append(p[u])
            # Go to p[u]
            u = p[u]

        # In the last loop, right before p[u] = v
        # the edge (v, p[u]) is not yet added
        # So, we perform it manually here
        list_of_node_in_cycle.append(p[u])
        edge_in_cycle = (u, v) # u is p[u] in the last loop
        w_of_edge = g.W[edge_in_cycle]
        edges_in_cycle_dict[edge_in_cycle] = w_of_edge

        # Find the edge in cycle with max weight
        [edge_max, weight_max] = max(edges_in_cycle_dict.items(), key=operator.itemgetter(1))
        # Remove this edge from MST
        MST.remove(edge_max[0], edge_max[1])
        # Add the removed edge to list
        edge_to_be_removed.append(edge_max)
        # Add the cycle to list
        list_of_cycles.append(list_of_node_in_cycle)
        # Start search for new cycle
        # Start search at vertex 1
        e = DFS(MST, vertex_to_start_search)
    return MST, list_of_cycles, edge_to_be_removed


if __name__ == "__main__":
    # Change the filename here to change graph
    filename = "G04PythonMST.txt"
    g = graph.Graph(filename)
    MST, cycles, edges = MSTCYCLE(g)

    print("Discovered cycles and removed edges")
    N = len(edges)
    if N == 0:
        print("No cycle")
    elif N > 0:
        for i in range(N):
            print(f"{i + 1}--{cycles[i]}---------{edges[i]}")

    print("Edge list of the minimal spanning tree")
    w_mst = 0
    edge_list = []
    for (u, v) in MST.W:
        if ((u, v) not in edge_list) and (v, u) not in edge_list:
            edge_list.append((u, v))
            w_mst += MST.W[(u, v)]

    print(edge_list)
    # In G1 and G5, there is multiple MST
    # So, check the weight is the best method to verify that the returned spanning tree is MST
    # G1 w_mst = 26
    # G2 w_mst = 9
    # G3 w_mst = 6
    # G4 w_mst = 17
    print("Weight of the minimal spanning tree")
    print(w_mst)
