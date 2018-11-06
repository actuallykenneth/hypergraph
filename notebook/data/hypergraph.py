from collections import defaultdict
from itertools import permutations

class HyperGraph:
    
    nodes = {}
    edges = {}
    total_node_count = 0
    total_edge_count = 0
    edge_permutations = []
    node_permutations = []
    edge_counts = {}
    node_counts = {}
    
    
    def __init__(self, nodes_dict={}, edges_dict={}):
        '''Requires a dictionary (key-->list) of nodes and edges'''
        self.nodes = nodes_dict
        self.edges = edges_dict
        
    
    def read_hypergraph_from_file(self, filename, sort_nodes=False):
        '''Reads a hypergraph in from a file.
        Format of a hypergraph in plaintext is: "EDGE_NUMBER NODE,NODE,NODE"
        Note that there is a whitespace delimiting the edge from the comma delimited nodes

        args: sort_nodes
            Will sort the nodes in the list if this is set to true
        '''
        the_node_counts = {}
        the_edge_counts = {}
        
        # initialize dictionaries that have empty lists as the default items
        the_edges = defaultdict(list)
        the_nodes = defaultdict(list)
        the_node_counts = defaultdict(int)
        the_edge_counts = defaultdict(int)
        # read the contents of the graph file
        file_contents = open(filename).readlines()
        for line in file_contents:
            # split the line into the node and the list of edges containing node
            line_split = line.split(' ')
            # first item delimited by whitespace is the node
            node = line_split[0]
            # second item is a comma delimited string of the edges containg node
            edge_line = line_split[1].strip();
            # split the string into a list of the edges
            edge_list = edge_line.split(',')
            # iterate through the edge list in the line
            for edge in edge_list:
                # build the dictionaries
                the_nodes[node].append(edge)
                # If it is an edgeless node, assign an empty list (length 0)
                if edge == '':
                    the_nodes[node] = []
                the_edges[edge].append(node)
                

                # build a dictionary of the counts
                the_node_counts[node] = len(the_nodes[node])
                the_edge_counts[edge] = len(the_edges[edge])
        
        # Delete the lone vertices        
        del the_edges['']
        del the_edge_counts['']
        
        # set the fields
        self.nodes = the_nodes
        self.edges = the_edges
        self.total_node_count = len(the_nodes)
        self.total_edge_count = len(the_edges)
        self.node_counts = the_node_counts
        self.edge_counts = the_edge_counts
    
    def generate_edge_permutations(self):
        the_edge_permutations = permutations(self.edges)
        self.edge_permutations = list(the_edge_permutations)
        
    def generate_node_permutations(self):
        the_node_permutations = permutations(self.nodes)
        self.node_permutations = list(the_node_permutations)
        
    def is_isomorphic_with(self, other_hypergraph):
        edge1 = dict.copy(self.edges)
        e_perm2 = other_hypergraph.edge_permutations
        node1 = dict.copy(self.nodes)
        other_node_permutations = other_hypergraph.node_permutations

        for perm in other_node_permutations:
                node1 = dict.copy(self.nodes)
                thing_we_want = defaultdict(list)
                for i, k, in enumerate(list(node1)):
                    node1[perm[i]] = node1[k]
                    del node1[k]



                for k, v in node1.items():
                    for item in v:
                        thing_we_want[item].append(k)


        #         print(thing_we_want)


                for perm in e_perm2:
                    edge2 = dict.copy(thing_we_want)
                    for i, k in enumerate(list(edge2)):
                        edge2[perm[i]] = edge2[k]
                        del edge2[k]


                    found = True
                    for key, value in edge2.items():
                        if (set(value) != set(other_hypergraph.edges[key])):
                            found = False
                    if found == True:
                        print(edge2)
                        print()
                        print(thing_we_want)
                        print()
                        print(edge1)
                        print()
                        for k,k2 in zip(thing_we_want, edge2):
                            if set(thing_we_want[k]) == set(edge2[k2]):
                                print(k, ':', k2)
                        print()
                        node_maps = []
                        for k,v in thing_we_want.items():
                            for i,value in enumerate(v):

                                node_maps.append((value, ':', edge1[k][i]))
                        print(set(node_maps))


HG1 = HyperGraph()
HG1.read_hypergraph_from_file('hypergraph1.txt')
HG1.generate_edge_permutations()
HG1.generate_node_permutations()

HG2 = HyperGraph()
HG2.read_hypergraph_from_file('hypergraph2.txt')
HG2.generate_edge_permutations()
HG2.generate_node_permutations()

HG1.is_isomorphic_with(HG2)