# This will work if ran from the root folder.
import sys 
sys.path.append("delivery_network")
from graph import Graph, graph_from_file
import unittest   # The test framework


"""
Premier test avec network 1
"""
class Test_Reachability(unittest.TestCase):
    def test_network1(self):
        g = graph_from_file("input/network.1.in")
        self.assertEqual(g.min_power(1, 20), ([1, 8, 20], 13))

if __name__ == '__main__':
    unittest.main()

"""
Second test avec un graph créé
"""
