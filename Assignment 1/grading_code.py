import os

def readfile(filename, type):

    V = {}
    """ input method for files """
    ff = open(filename, 'r')
    for ll in ff.readlines():
        try:
            u = int(ll.split(':')[0].strip())
        except:
            continue
        if u not in V:
            V[u] = []
        for vv in ll.split(':')[1].split():
            try:
                v = int(vv)
            except:
                continue
            if v not in V:
                V[v] = []
            V[u].append(v)

    return V


def grading(output_directory, solution_directory):

    nb_generate_trees = len(os.listdir(output_directory))
    nb_solution_trees = len(os.listdir(solution_directory))
    print("\nCheck numbers of generated trees and solution trees")
    print(f"Generated trees: {nb_generate_trees} trees.")
    print(f"Solution trees: {nb_solution_trees} trees.\n\n")

    if nb_generate_trees != nb_solution_trees:
        print("PLEASE CHECK YOUR CODE.\n\n")

    already_matched_file = []

    for out_file in os.scandir(output_directory):
        adj_list_output = readfile(out_file, "json")

        for sol_file in os.scandir(solution_directory):
            if sol_file in already_matched_file:
                break

            adj_list_solution = readfile(sol_file, "not_json")

            if adj_list_output == adj_list_solution:
                output_filename = out_file.name.split('\\')[-1]
                solution_filename = sol_file.name.split('\\')[-1]

                already_matched_file.append(solution_filename)

                print(f"{output_filename} <-> {solution_filename}")
                break

    missing_trees = []
    for sol_file in os.scandir(solution_directory):
        solution_filename = sol_file.name.split('\\')[-1]

        if solution_filename not in already_matched_file:
            missing_trees.append(solution_filename)

    print(f"\nTHERE ARE {len(missing_trees)} MISSING TREES.")
    for miss_filename in missing_trees:
        print(miss_filename)


if __name__ == "__main__":
    print("Usage:\n"
          "1. Create a folder name \"output\" (you may change the name) in the current directory.\n\n"
          "2. Run the code that generated all trees for one graph and one start vertex, place all\n"
          "trees in \"output\" folder.\n\n"
          "3. Run the code in IDE or type in the command line open in the current directory: \n"
          "\"python grading_code.py\"\n\n"
          "4. Enter the name \"output\" for\n the output directory.\n\n"
          "5. For solution directory, enter relative path of folder contained the solution trees\n"
          "(Example: something\\PyG10Start1) or go into File Explorer and copy the path then\n"
          "paste here.\n\n")
    output_dir = input("output directory: ")
    solution_dir = input("Solution tree directory: ")

    grading(output_dir, solution_dir)

    print("\nMAYBE YOU WANT TO DELETE OLD FILES BEFORE CONTINUING.")
