from graph import Graph, graph_from_file
import time

data_path = "../input/"
file_name = "network.2.in"

#g = graph_from_file(file_name)
#print(g)


h = graph_from_file("input/network.2.in")
h.kruskal()


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
 
print(temps_routes("input/routes.2.in","input/network.2.in"))
"""
"""
debut = time.perf_counter()
print(h.min_power(1220, 46952))
fin = time.perf_counter()

print(fin-debut)
"""

