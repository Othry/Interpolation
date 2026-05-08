# dummy, dummy

import unittest
import numpy as np
from Base_code import LagrangeInterpolation

class LagrangeInterpolationTest(unittest.TestCase):
    def setUp(self):
        self.nodes = [0.0, 1.0, 2.0]
    
    def test_lagrange_nodes(self):
        for k in range(len(self.nodes)):
            #erzeugt kronecker delta
            y_values = np.zeros(len(self.nodes))
            y_values[k] = 1.0

            pol = LagrangeInterpolation(self.nodes, y_values)

            #vektorisierte auswertung mit np
            res = pol(self.nodes)
            np.testing.assert_array_equal(res, y_values)
    
    def test_random_points_sum(self):
        y_ones = np.ones(len(self.nodes))
        pol = LagrangeInterpolation(self.nodes, y_ones)
        #Erzeugt test_values skaliert auf das konkrete Intervall
        test_values = np.random.rand(100) * (max(self.nodes) - min(self.nodes)) + min(self.nodes)

        res = pol(test_values)
        expected = np.ones_like(test_values)

        np.testing.assert_allclose(res, expected)

    
    def test_polynom_identity(self):
        def test_pol(x):
            return x**2
        
        nodes_arr = np.array(self.nodes)
        y_values = test_pol(nodes_arr)
        
        pol = LagrangeInterpolation(self.nodes, y_values)
        test_values = np.random.rand(100) * (max(self.nodes) - min(self.nodes)) + min(self.nodes)

        res = pol(test_values)
        expected = test_pol(test_values)

        np.testing.assert_allclose(res, expected)

if __name__ == '__main__':
    unittest.main()