# This will work if ran from the root folder.
import sys
sys.path.append("delivery_network")
 
from graph import Graph, graph_from_file
 
import unittest   # The test framework
 
class Test_Reachability(unittest.TestCase):
    def test_network1(self):
        g = graph_from_file("input/network.1.in")
        self.assertEqual(g.Dijkstra(1,2,1), None)
        self.assertEqual(g.Dijkstra(1,2,10), [1,2])
        self.assertEqual(g.Dijkstra(1,2,60), [1, 14, 2])
if __name__ == '__main__':
    unittest.main()
