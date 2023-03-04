class Graph:
    """
    A class representing graphs as adjacency lists and implementing various algorithms on the graphs. Graphs in the class are not oriented. 
    Attributes: 
    -----------
    nodes: NodeType
        A list of nodes. Nodes can be of any immutable type, e.g., integer, float, or string.
        We will usually use a list of integers 1, ..., n.
    graph: dict
        A dictionnary that contains the adjacency list of each node in the form
        graph[node] = [(neighbor1, p1, d1), (neighbor1, p1, d1), ...]
        where p1 is the minimal power on the edge (node, neighbor1) and d1 is the distance on the edge
    nb_nodes: int
        The number of nodes.
    nb_edges: int
        The number of edges. 
    """

    def __init__(self, nodes=[]):
        """
        Initializes the graph with a set of nodes, and no edges. 
        Parameters: 
        -----------
        nodes: list, optional
            A list of nodes. Default is empty.
        """
        self.nodes = nodes
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0

    def __str__(self):
        """Prints the graph as a list of neighbors for each node (one per line)"""
        if not self.graph:
            output = "The graph is empty"            
        else:
            output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n"
            for source, destination in self.graph.items():
                output += f"{source}-->{destination}\n"
        return output
    
    def add_edge(self, node1, node2, power_min, dist=1):
        """
        Adds an edge to the graph. Graphs are not oriented, hence an edge is added to the adjacency list of both end nodes. 
        Parameters: 
        -----------
        node1: NodeType
            First end (node) of the edge
        node2: NodeType
            Second end (node) of the edge
        power_min: numeric (int or float)
            Minimum power on this edge
        dist: numeric (int or float), optional
            Distance between node1 and node2 on the edge. Default is 1.
        """
        if node1 not in self.graph:
            self.graph[node1] = []
            self.nb_nodes += 1
            self.nodes.append(node1)
        if node2 not in self.graph:
            self.graph[node2] = []
            self.nb_nodes += 1
            self.nodes.append(node2)

        self.graph[node1].append((node2, power_min, dist))
        self.graph[node2].append((node1, power_min, dist))
        self.nb_edges += 1
    
    def voisin_acc(self, node1, power):
        v = []
        for i in g.graph[node1]:
            if i[1] <= power:
                v.append(i[0])
        return v

    def get_path_with_power_bis(self, src, dest, power, trajet):
        
        #On vérifie si src et dest sont dans le même composante connexe
        for i in self.connected_components():
            if src in i:
                if dest not in i:
                    return None

    
        t = trajet


        for i in self.voisin_acc(src, power) :

            if i not in t :
                t.append(i)
                if i == dest:
                    return t 
                else : 
                    return self.get_path_with_power_bis(i, dest, power, t)
                t.pop()
        return None
        
    def get_path_with_power(self, src, dest, power):
        t = [src]
        return self.get_path_with_power_bis(src, dest, power, t)
        
    def parcours_en_profondeur(self, node, seen=None):
        if seen is None:
            seen = []
        if node not in seen:
            seen.append(node)
            unseen = []
            for t in self.graph[node]:
                if t[0] not in seen:
                    unseen.append(t[0])
            for node in unseen:
                self.parcours_en_profondeur(node, seen)
        return seen

    def connected_components(self):
        ccs = []
        for node in self.nodes:
            if ccs == []:        
                ccs.append(self.parcours_en_profondeur(node))
            else:
                a = True
                for cc in ccs:
                    if node in cc:
                        a = False
                if a:
                    ccs.append(self.parcours_en_profondeur(node))
        return ccs

    def connected_components_set(self):
        """
        The result should be a set of frozensets (one per component), 
        For instance, for network01.in: {frozenset({1, 2, 3}), frozenset({4, 5, 6, 7})}
        """
        return set(map(frozenset, self.connected_components()))
    
    def min_power(self, src, dest):
        """
        Should return path, min_power. 
        """
        a = 0
        b = 100
        c = 0

        while b != a:    
            c = int((b+a)/2)
            if self.get_path_with_power(src, dest, c) is None:
                a = c
            else:
                b = c    
        return self.get_path_with_power(src, dest, c), c



def graph_from_file(filename):
 
    with open(filename, "r") as file:
        n, m = map(int, file.readline().split())
        g = Graph(range(1, n+1))
        for _ in range(m):
            edge = list(map(int, file.readline().split()))
            if len(edge) == 3:
                node1, node2, power_min = edge
                g.add_edge(node1, node2, power_min) # will add dist=1 by default
            elif len(edge) == 4:
                node1, node2, power_min, dist = edge
                g.add_edge(node1, node2, power_min, dist)
            else:
                raise Exception("Format incorrect")
    return g


g = Graph([k for k in range(10)])

g.add_edge(1, 5, 20)
g.add_edge(1, 2, 10)
g.add_edge(2, 5,15)
g.add_edge(2, 3, 10)
g.add_edge(3, 5, 10)

print(g.min_power(1, 5))
