# This will work if ran from the root folder.
import sys 
sys.path.append("delivery_network")

from graph import Graph, graph_from_file

import unittest   # The test framework

class Test_Reachability(unittest.TestCase):
    def test_network1(self):
        g = graph_from_file("input/network.1.in")
        self.assertEqual(g.get_path_with_power(1, 12, 50), [1, 8, 3, 11, 2, 12])

if __name__ == '__main__':
    unittest.main()
