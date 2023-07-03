import sys

def read_instance(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            array = []
            for l in lines:
                if l.startswith("#"): continue
                array.append([int(i) for i in l.split()])
            return array

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
    except Exception as e:
        print("An error occurred while reading the file:", e)
        return None

def pos_min(a, b):
    if b == -1:
        return a
    elif a == -1:
        return b
    else:
        return min(a, b)

# Some notes:
# -----------
# A depth-first search defines a spanning forest - we call the edges in this the "tree edges".
# 
# Edges that run from descendents to anscestors within the same tree are called "fronds"
#
# Edges that run between subtrees are called "cross-links"
#  
# For a node v, lowlink[v] is maintained as the earliest visited node that is reachable by traversing 0 or
# more tree edges followed by at most one frond or cross-link
#
# Strongly-connected components (SCCs) are subtrees of the spanning forest obtained from DFS.
# In particular, a node is a root of an SCC if lowlink[v] = number[v], where number[v] is the
# visitation number of v in the DFS.
def strong_connect(adj, v, count, stack, lowlink, number):
    lowlink[v] = count
    number[v] = count
    count += 1
    stack.append(v)
    sccs = []
    for w in adj[v]:
        if number[w] == -1:
            # (v, w) is a tree edge
            count, new_sccs = strong_connect(adj, w, count, stack, lowlink, number)
            sccs.extend(new_sccs)
            lowlink[v] = pos_min(lowlink[v], lowlink[w])

        elif number[w] < number[v]:
            # (v, w) is a frond or a cross-link
            if w in stack:
                lowlink[v] = pos_min(lowlink[v], number[w])
    
    if lowlink[v] == number[v]:
        # v is the root of a component
        new_scc = []
        while len(stack) > 0 and number[stack[-1]] >= number[v]:
            new_scc.append(stack.pop())
        sccs.append(new_scc)

    return count, sccs

def find_sccs(adj):
    count = 0
    stack = []
    lowlink = [-1]*len(adj)
    number = [-1]*len(adj)
    sccs = []
    for v in range(len(adj)):
        if number[v] == -1:
            count, new_sccs = strong_connect(adj, v, count, stack, lowlink, number)
            sccs.extend(new_sccs)
    return sccs

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Please provide the file path as an argument.")
    else:
        file_path = sys.argv[1]
        adj = read_instance(file_path)
        sccs = find_sccs(adj)
        for component in sccs:
            print(component)
        
