
from graph import Graph, graph_from_file
import time
# import graphviz
# from graphviz import Digraph

data_path = "../input/"


def temps_routes(filename, filename2):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    n = len(lines)
    h = graph_from_file(filename2)
    linesp = lines[1:min(n, 10)+1]
    debut = time.perf_counter()
    for line in linesp:
        print(line)
        words = line.split()
        h.min_power(int(words[0]), int(words[1]))
    fin = time.perf_counter()
    return ((fin-debut)*max(n/10, 1))

def temps_routes_opti(filename, filename2):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    n = len(lines)
    h = graph_from_file(filename2)
    linesp = lines[1:min(n, 10)+1]
    b = h.kruskal()
    profondeurs, parents = b.find_parents(1)
    debut = time.perf_counter()
    for line in linesp:
        #print(line)
        words = line.split()
        b.min_power_opti(int(words[0]), int(words[1]), profondeurs, parents)
    fin = time.perf_counter()
    return ((fin-debut)*max(n/10, 1))
    
#print(temps_routes_opti("input/routes.9.in","input/network.9.in"))





