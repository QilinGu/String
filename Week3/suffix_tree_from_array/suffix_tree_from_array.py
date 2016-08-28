# python3
import sys


class SuffixTreeNode:
    def __init__(self, parent, children, string_depth, edge_start, edge_end):
        self.parent = parent
        self.children = children
        self.string_depth = string_depth
        self.edge_start = edge_start
        self.edge_end = edge_end


def create_new_leaf(node, text, suffix):
    leaf = {'parent': node,
              'children': {},
              'string_depth': len(text) - suffix,
              'edge_start' :suffix + node['string_depth'],
              'edge_end': len(text) - 1}
    node['children'][text[node['edge_start']]] = leaf


def break_edge(node, text, start, offset):
    start_char = text[start]
    mid_char = text[start + offset]
    mid_node = {'parent': node,
         'children': {},
         'string_depth': node['string_depth'] + offset,
         'edge_start': start + offset,
         'edge_end': node['children'][start_char]['edge_end']}
    mid_node['children'][mid_char] = node['children'][start_char]
    node['children'][start_char]['parent'] = mid_node
    node['children'][start_char] = mid_node
    return mid_node


def suffix_array_to_suffix_tree(sa, lcp, text):
    """
    Build suffix tree of the string text given its suffix array suffix_array
    and LCP array lcp_array. Return the tree as a mapping from a node ID
    to the list of all outgoing edges of the corresponding node. The edges in the
    list must be sorted in the ascending order by the first character of the edge label.
    Root must have node ID = 0, and all other node IDs must be different
    nonnegative integers. Each edge must be represented by a tuple (node, start, end), where
        * node is the node ID of the ending node of the edge
        * start is the starting position (0-based) of the substring of text corresponding to the edge label
        * end is the first position (0-based) after the end of the substring corresponding to the edge label

    For example, if text = "ACACAA$", an edge with label "$" from root to a node with ID 1
    must be represented by a tuple (1, 6, 7). This edge must be present in the list tree[0]
    (corresponding to the root node), and it should be the first edge in the list (because
    it has the smallest first character of all edges outgoing from the root).
    """
    tree = {}
    root = {
        'parent' :None,
        'children': {},
        'string_depth': 0,
        'edge_start': 0,
        'edge_end': 0
    }
    lcp_prev = 0
    cur_node = root
    for i in range(len(sa)):
        suffix = sa[i]
        while cur_node['string_depth'] > lcp_prev:
            cur_node = cur_node['parent']
        if cur_node['string_depth'] == lcp_prev:
            create_new_leaf(cur_node, text, suffix)
        else:
            edge_start = sa[i - 1] + cur_node['string_depth']
            offset = lcp_prev - cur_node['string_depth']
            mid_node = break_edge(cur_node, text, edge_start, offset)
        if i < len(text) -1:
            lcp_prev = lcp[i]
    # Implement this function yourself
    print(root)
    return tree


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    sa = list(map(int, sys.stdin.readline().strip().split()))
    lcp = list(map(int, sys.stdin.readline().strip().split()))
    print(text)
    # Build the suffix tree and get a mapping from 
    # suffix tree node ID to the list of outgoing Edges.
    tree = suffix_array_to_suffix_tree(sa, lcp, text)
    print(tree)
    """
    Output the edges of the suffix tree in the required order.
    Note that we use here the contract that the root of the tree
    will have node ID = 0 and that each vector of outgoing edges
    will be sorted by the first character of the corresponding edge label.
    
    The following code avoids recursion to avoid stack overflow issues.
    It uses two stacks to convert recursive function to a while loop.
    This code is an equivalent of 
    
        OutputEdges(tree, 0);
    
    for the following _recursive_ function OutputEdges:
    
    def OutputEdges(tree, node_id):
        edges = tree[node_id]
        for edge in edges:
            print("%d %d" % (edge[1], edge[2]))
            OutputEdges(tree, edge[0]);
    
    """
    stack = [(0, 0)]
    result_edges = []
    while len(stack) > 0:
      (node, edge_index) = stack[-1]
      stack.pop()
      if not node in tree:
        continue
      edges = tree[node]
      if edge_index + 1 < len(edges):
        stack.append((node, edge_index + 1))
      print("%d %d" % (edges[edge_index][1], edges[edge_index][2]))
      stack.append((edges[edge_index][0], 0))
