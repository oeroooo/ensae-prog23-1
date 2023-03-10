from graph import Graph, graph_from_file
import time

data_path = "../input/"
file_name = "network.01.in"

#g = graph_from_file(file_name)
#print(g)


h = graph_from_file("input/network.00.in")

debut = time.perf_counter()
print(h.min_power(1, 9))
fin = time.perf_counter()

print(fin-debut)

