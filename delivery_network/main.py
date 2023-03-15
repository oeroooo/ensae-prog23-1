

"""
A faire
-min_power mst avec get_path amélioré
-Amélioré les fonctions précédentes
-Refaire get_path_with_power
-distance
-Nettoyer code
-Rendre accessible à tous le github
-Fichier test
-Fichier réponse aux questions



"""



from graph import Graph, graph_from_file
import time
import graphviz
from graphviz import Digraph

data_path = "../input/"
file_name = "network.2.in"

"""
dot = graphviz.Digraph(comment='The Round Table')
dot.node('A', 'King Arthur')  # doctest: +NO_EXE
dot.node('B', 'Sir Bedevere the Wise')
dot.node('L', 'Sir Lancelot the Brave')
dot.render('exemple_graphique', view=True)
"""

def temps_routes(filename, filename2):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    n= len(lines)
    h= graph_from_file(filename2)
    linesp=lines[1:min(n, 10)+1]
    debut = time.perf_counter()
    for line in linesp:
        print(line)
        words = line.split()
        h.min_power(int(words[0]), int(words[1]))
    fin = time.perf_counter()
    return ((fin-debut)*max(n/10,1))
    
#print(temps_routes("input/routes.2.in","input/network.2.in"))  


def temps_routes_opti(filename, filename2):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    n= len(lines)
    h= graph_from_file(filename2)
    linesp=lines[1:min(n, 10)+1]
    b = h.kruskal()
    profondeurs, parents = b.find_parents(1)
    debut = time.perf_counter()
    for line in linesp:
        print(line)
        words = line.split()
        b.get_path_opti(int(words[0]), int(words[1]), profondeurs, parents)
    fin = time.perf_counter()
    return ((fin-debut)*max(n/10,1))
    
#print(temps_routes_opti("input/routes.9.in","input/network.9.in"))  

"""
def temps_routes(filename, filename2):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    n= len(lines)
    h= graph_from_file(filename2)
    linesp=lines[1:min(n, 10)+1]
    debut = time.perf_counter()
    for line in linesp:
        print(line)
        words= line.split()
        h.min_power(int(words[0]), int(words[1]))
    fin = time.perf_counter()
    return ((fin-debut)*max(n/10,1))
 
#print(temps_routes("input/routes.2.in","input/network.2.in"))
"""

"""
debut = time.perf_counter()
print(h.min_power(1220, 46952))
fin = time.perf_counter()

print(fin-debut)
"""


