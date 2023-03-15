"""
-----------------------
Ce document est un brouillon.
Sont stockés ici des morceaux de codes et de test
Le contenu de ce fichier n'est pas à prendre en compte dans la correction.
Il a uniquement pour but de ne pas polluer les autres fichiers
------------------------

"""



"""
Ne fonctionne pas
dot = graphviz.Digraph(comment='The Round Table')
dot.node('A', 'King Arthur')  # doctest: +NO_EXE
dot.node('B', 'Sir Bedevere the Wise')
dot.node('L', 'Sir Lancelot the Brave')
dot.render('exemple_graphique', view=True)
"""


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

