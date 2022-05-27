from graafi3 import Graph
from BFS import BFS
import os


def N_possible_trees(parent_dict):
    """Count the number of possible min path trees"""
    N = 1
    for parent in parent_dict.values():
        n = max(len(parent), 1)
        N = N * n
    return N


def parentDict(g, s):
    """Create a dict of parent of nodes"""
    B = BFS(g, s)
    parent_dict = {}
    for node in B.keys():
        adj = g.adj(node)
        potent_parent = [x for x in B if B[x] == B[node] - 1]
        parent = list(set(adj) & set(potent_parent))
        parent_dict[node] = parent
    return parent_dict


def tree2dict(tree):
    """Convert a tree to a adj dict"""

    adj_dict = {}
    for node, parent in tree.items():
        if parent not in adj_dict.keys():
            adj_dict[parent] = [node]
        else:
            adj_dict[parent].append(node)
    return adj_dict


def writefile(index, tree):
    """Write an edge list to a file"""
    filename = f"output/tree{index}.txt"
    ff = open(filename, "w")
    adj_dict = tree2dict(tree)
    i = 0
    for u in adj_dict.keys():
        i += 1
        ff.write(str(u))
        ff.write(": ")
        for v in adj_dict[u]:
            ff.write(str(v))
            ff.write(" ")
        if i < len(adj_dict):
            ff.write('\n')


def allMinSpanT(g, s):
    """Return a dictionary of all possible edge lists and write files"""
    parent_dict = parentDict(g, s)
    N = N_possible_trees(parent_dict)

    # Set up a list of N possible trees
    trees_list = [{} for i in range(N)]
    # A tree is a dictionary with keys is the node and value of key is the parent of the node

    # Start combining all possible trees
    # We use 4 loop to write all possible combination of sets
    # loop 1
    temp = N
    for node in g.V:
        nb_edges = len(parent_dict[node])

        # In case the node is not in the same components with the source
        if nb_edges == 0:
            if node == s:
                continue
            for i in range(N):
                trees_list[i][node] = None
        else:
            n = temp // nb_edges
            # Loop 2
            ith_tree = 0
            while ith_tree < N:
                # Loop 3
                for parent in parent_dict[node]:
                    # Loop 4
                    # Write a parent value n times before move
                    # to the new one.
                    for i in range(n):
                        trees_list[ith_tree][node] = parent
                        ith_tree += 1
            temp = n

    # Write to files
    # Empty the output directory first
    dr = "output/"
    for f in os.listdir(dr):
        os.remove(os.path.join(dr, f))

    for i in range(N):
        writefile(i, trees_list[i])
    return trees_list


if __name__ == "__main__":
    g = Graph('G11Python.txt')
    T = allMinSpanT(g, 1)
    for item in T:
        print(item)
