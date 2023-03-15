

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
        self.edges = []

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
        self.edges.append([node1, node2, power_min, dist])
    
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

        """
        Cette fonction visite tous les sommets du graph accessibles par des arêtes à partir du 
        point de dépar de manière
        récursive. On explore chaque branche et si on finit d'explorer
        une branche, on revient autant en arrière que nécessaire
        pour trouver des sommets que l'on a pas encore vu
        
        Paramètres: 
        -----------
        node: NodeType
            Point de départ du parcours en profondeur
        seen: list or Nonetype, optional
            Donne les noeuds déjà vu, évite de revenir sur nos pas dans
            la recherche d'un voisin
            Par défaut seen = None

        Résultats :
        -----------
        Liste de tous les sommets parcourus (qui sont donc les sommets
        réliés par un chemin existant au sommet initial)
        """

        if seen is None:
            #Si on a rien vu pour l'instant on initialise avec une liste vide
            seen = []
        if node not in seen: #On vérifie qu'on a pas déjà vu le sommet
            seen.append(node)
            unseen = []
            for t in self.graph[node]:
                if t[0] not in seen:
                    unseen.append(t[0])
            for node in unseen: #On travaille par récursivité
                self.parcours_en_profondeur(node, seen)
        return seen

    def connected_components(self):

        """
        Cette fonction donne les composantes connexes d'un graphe.
        On prend un premier sommet, on trouve grâce au parcours en
        profondeur tous les sommets accessibles et qui sont donc
        dans la même composante connexe. Une fois cela fait
        on prend le premier sommet qui n'est pas déjà dans une composante
        connexe, et on refait la même opération

        Paramètres: 
        -----------

        Résultats :
        -----------
        Liste de listes (chacune des listes représente une composante connexe)

        """
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
            c = (b + a) // 2

            if self.get_path_with_power(src, dest, c) is None:
                a = c + 1
            else:
                b = c   
        return self.get_path_with_power(src, dest, b), b
  
    def find(self, parent, x):
        if parent[x] == x:
            return x
        return self.find(parent, parent[x])  

    def union(self, parent, rang, x, y):
        xracine = self.find(parent, x)
        yracine = self.find(parent, y)
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

        """
        On pouvait utiliser cette méthode pour récupérer la liste de toutes les arêtes
        et ensuite les trier. Mais il apparaissait plus rapide de conserver les arêtes dans une liste
        créer au moment de la création du graph. 

        liste_arete = []
        seen = []
        for i in self.nodes:
            for j in self.graph[i]:

                a = j[0]
                b = j[1]

                if [i, a] and [a, i] not in seen:
                    seen.append([i, a])

                    liste_arete.append([i, a, b])
        """

        liste_arete = self.edges
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

        return g_mst

    def get_path_mst(self, src, dest):

        """
        Dans un arbre couvrant minimal le chemin entre deux sommets
        est toujours unique. Nous n'avons donc plus besoin d'effectuer
        les vérifications de power, ce qui améliore grandement
        la complexité de l'algorithme
        """       
        seen = []
        stack = [(src, [src], [])]
        while stack:
            (node, chemin, power) = stack.pop()
            if node == dest:
                return chemin, power
            if node not in seen:
                seen.append(node)
                for voisin in self.graph[node]:
                    a = (voisin[0], chemin + [voisin[0]], power + [voisin[1]])
                    stack.append(a)
        return None

    def min_power_mst(self, src, dest):
        """
        On supposer que min_power_mst est utilisé uniquement
        pour des arbres couvrant minimaux
        """
        chemin, power = self.get_path_mst(src, dest) 
        return max(power)

    def root(self, rang, src):
        a = self.graph
        return rang.index(max(rang[i[0]] for i in a[src]))  

    def find_parents(self, start):

        parents = {} 
        profondeur = dict([(sommet, 0) for sommet in self.nodes])
        deja_vu = dict([(sommet, False) for sommet in self.nodes])
        # On fixe des valeurs initiales pour le point de départ
        deja_vu[start] = True
        parents[start] = [start, -1]

        arbre = self.graph

        def find_parents_auxiliaires(graph, node):
            for neighbor, power, distance in graph[node]:
                if not deja_vu[neighbor]:
                    deja_vu[neighbor] = True
                    parents[neighbor] = [node, power]
                    profondeur[neighbor] = profondeur[node] + 1
                    find_parents_auxiliaires(graph, neighbor)

        find_parents_auxiliaires(arbre, start)

        return profondeur, parents

    def get_path_opti(self, src, dest, profondeurs, parents):

        prof_src = profondeurs[src]
        prof_dest = profondeurs[dest]
        pathsrc = [src]
        powerpathsrc = []
        pathdest = [dest]
        powerpathdest = []

        tree = self.graph

        if prof_src > prof_dest:
            for i in range(prof_src - prof_dest):
                p = parents[pathsrc[-1]][0]
                power = parents[pathsrc[-1]][1]
                pathsrc.append(p)
                powerpathsrc.append(power)
        elif prof_dest > prof_src:
            for i in range(prof_dest - prof_src):
                p = parents[pathdest[-1]][0]
                power = parents[pathdest[-1]][1]
                pathdest.append(p)
                powerpathdest.append(power)
        while pathdest[-1] != pathsrc[-1]:
            p1 = parents[pathsrc[-1]]
            p2 = parents[pathdest[-1]]
            pathsrc.append(p1[0])
            powerpathsrc.append(p1[1])
            pathdest.append(p2[0])
            powerpathdest.append(p2[1])  

        if len(pathsrc) != 1 and len(pathdest) != 1:
            pathdest.reverse()
            powerpathdest.reverse()
            pathfinal = pathsrc + pathdest[1:]
            powerfinal = powerpathsrc + powerpathdest[1:]
        
        if len(pathdest) == 1:
            pathfinal = pathsrc
            powerfinal = powerpathsrc
        
        if len(pathsrc) == 1:
            pathdest.reverse()
            powerpathdest.reverse()
            pathfinal = pathdest[1:]
            powerfinal = powerpathdest[1:]

        return pathfinal, max(powerfinal)


def graph_from_file(filename):
    with open(filename, "r") as file:
        n, m = map(int, file.readline().split())
        g = Graph(range(1, n+1))
        for _ in range(m):
            edge = list(map(int, file.readline().split()))
            if len(edge) == 3:
                node1, node2, power_min = edge
                g.add_edge(node1, node2, power_min)  # will add dist=1 by default
            elif len(edge) == 4:
                node1, node2, power_min, dist = edge
                g.add_edge(node1, node2, power_min, dist)
            else:
                raise Exception("Format incorrect")
    return g



g = Graph([k for k in range(5)])

g.add_edge(0, 1, 10)
g.add_edge(1, 2, 10)
g.add_edge(1, 3, 15)
g.add_edge(1, 5, 15)
g.add_edge(5, 6, 15)
g.add_edge(2, 4, 10)
g.add_edge(3, 4, 10)

g2 = g.kruskal()


a , b = g2.find_parents(1)

#print(g2.get_path_opti(3, 6, a, b))

#print(g)
#print(g.graph)
#print(g.edges)
#a, b = g.kruskal()
#print(b)

#print(g.get_path_with_power(1, 4, 10))
#print(g.min_power(1, 4))
#b = g.kruskal()
#print(b.get_path_with_power(1, 4, 10))
#print(b.get_path_mst(1, 4))
#print(b.min_power_mst(1, 4))


#print(g.min_power(1, 4))
#print(g.min_power_mst(1, 4))


"""
h = graph_from_file("input/network.2.in")
h.kruskal()
profondeurs, parents = h.find_parents(1)
print(h.get_path_opti(4, 5, profondeurs, parents))
"""




#print(h.get_path_with_power(1, 9, 50))
#print(h.min_power(1, 5))
#print(h.min_power_mst(1, 5))

