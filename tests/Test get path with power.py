# This will work if ran from the root folder.
import sys 
sys.path.append("delivery_network")

from graph import Graph, graph_from_file

import unittest   # The test framework

class Test_Reachability(unittest.TestCase):

    """
    On teste dans le fichier network 1 un trajet
    """
    def test_network1(self):
        g = graph_from_file("input/network.1.in")
        self.assertEqual(g.get_path_with_power(1, 12, 50), [1, 8, 3, 11, 2, 12])
        
        #L'arête entre 3 et 11 est de puissance 41, donc le chemin doit changer
        self.assertEqual(g.get_path_with_power(1, 12, 40), [1, 8, 3, 14, 7, 16, 12])

if __name__ == '__main__':
    unittest.main()
