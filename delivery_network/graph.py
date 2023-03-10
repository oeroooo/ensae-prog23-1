

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
        for i in self.graph[node1]:
            if i[1] <= power:
                v.append(i[0])
        return v

    def get_path_with_power(self, src, dest, power):
        
        seen = set()
        stack = [(src, [src])]

        while stack:
            (node, chemin) = stack.pop()
            if node == dest:
                return chemin
            if node not in seen:
                seen.add(node)
                for voisin in self.voisin_acc(node, power):
                    stack.append((voisin, chemin + [voisin]))
        return None

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
        t = 1
        while self.get_path_with_power(src, dest, t) is None:
            t = t*2     
        a = t // 2
        b = t
        c = 0
        while b > a:    
            c = (b + a) //2

            if self.get_path_with_power(src, dest, c) is None:
                a = c + 1
            else:
                b = c   
        return self.get_path_with_power(src, dest, b), b
  
    def find(self,parent,x):
        if parent[x] == x:
            return x
        return self.find(parent,parent[x])  

    def union(self,parent,rang,x,y):
        xracine = self.find(parent,x)
        yracine = self.find(parent,y)
        if rang[xracine] < rang[yracine]:
            parent[xracine] = yracine
        elif rang[xracine] > rang[yracine]:
            parent[yracine] = xracine
        else:
            parent[yracine] = xracine
            rang[xracine] += 1

    def kruskal(self):

        parent = []
        rang = []
        resultat = []

        g_mst = Graph()
        test = 0
        liste_arete = []
        seen = []
        for i in self.nodes:
            for j in self.graph[i]:
                test = test+1
                print(test)
                a = j[0]
                b = j[1]

                if [i, a] and [a, i] not in seen:
                    seen.append([i, a])

                    liste_arete.append([i, a, b])

        liste_croissante_arete = sorted(liste_arete, key=lambda x: x[2])

        V = self.nb_nodes

        for n in range(V+1):
            parent.append(n)
            rang.append(0)

        for i in liste_croissante_arete:
            if len(resultat) == V - 1:
                return g_mst
            x = self.find(parent, i[0])
            y = self.find(parent, i[1])
            if x != y:
                resultat.append(i)
                g_mst.add_edge(i[0], i[1], i[2])
                self.union(parent, rang, x, y)   
            print(resultat[-1]) 

        return g_mst



    def min_power_mst(self, src, dest):
        arbre = self.kruskal()
        return arbre.min_power(src, dest)


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

"""
g = Graph([k for k in range(5)])

g.add_edge(0, 1, 10)
g.add_edge(1, 2, 10)
g.add_edge(1, 3, 15)
g.add_edge(2, 4, 10)
g.add_edge(3, 4, 10)

#print(g)
#print(g.graph)
#print(g.kruskal())


print(g.min_power(1, 4))
print(g.min_power_mst(1, 4))
"""

"""
h = graph_from_file("input/network.00.in")
print(h.graph)
print(h.kruskal())


 
print(h.get_path_with_power(1, 9, 50))
print(h.min_power(1, 5))
print(h.min_power_mst(1, 5))

"""







"""    
    def get_path_with_power(self, src, dest, power):   
        #On vérifie si src et dest sont dans le même composante connexe
        for i in self.connected_components():
            if src in i:
                if dest not in i:
                    return None

        t = trajet
        print(t)

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
"""