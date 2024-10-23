import unittest
import numpy as np
import pandas as pd

class CalculsStatistiquesTestCase(unittest.TestCase):

    def setUp(self):
        data = {
            'A': [1, 2, 3, 4, 5],
            'B': [5, 6, 7, 8, 9],
            'C': [9, 10, 11, 12, 13]
        }
        self.df = pd.DataFrame(data)

    def test_mean(self):
        result = np.mean(self.df['A'])
        self.assertEqual(result, 3)

    def test_median(self):
        result = np.median(self.df['B'])
        self.assertEqual(result, 7)

    def test_std(self):
        result = np.std(self.df['C'])
        self.assertAlmostEqual(result, 1.41421356)

if __name__ == '__main__':
    unittest.main()
