# This will work if ran from the root folder.
import sys 
sys.path.append("delivery_network/")

import unittest 
from graph import Graph, graph_from_file

class Test_GraphLoading(unittest.TestCase):

    """
    On vérifie que l'arbre donné est bien
    V - 1 arêtes avec V le nombre de noeuds du graph
    initial

    """
    def test_network1(self):
        g = graph_from_file("input/network.1.in")
        g_mst = g.kruskal()
        self.assertEqual(g_mst.nb_edges, g.nb_nodes-1)
        
    def test_network2(self):
        g = graph_from_file("input/network.3.in")
        g_mst = g.kruskal()
        self.assertEqual(g_mst.nb_edges, g.nb_nodes-1)


if __name__ == '__main__':
    unittest.main()
