
import sys 
sys.path.append("delivery_network")

from graph import Graph, graph_from_file

import unittest   # The test framework

class Test_GraphLoading(unittest.TestCase):
    def test_network04(self):
        g = graph_from_file("input/network.04.in")
        self.assertEqual(g.nb_nodes, 10)
        self.assertEqual(g.nb_edges, 4)
        self.assertEqual([t[2] for t in g.graph[1]],[6,89])
        self.assertEqual([t[2] for t in g.graph[2]],[3,89])
        self.assertEqual([t[2] for t in g.graph[3]],[3,2])
        self.assertEqual([t[2] for t in g.graph[4]],[2,6])

if __name__ == '__main__':
    unittest.main()
