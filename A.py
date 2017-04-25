import unittest


class A(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(1,2)
    def test_valid1(self):
        self.assertEqual(2,2)

    @staticmethod
    def suite():
        suite = unittest.TestLoader().loadTestsFromTestCase(A)
        unittest.TextTestRunner(verbosity=2).run(suite)
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(A)
    unittest.TextTestRunner(verbosity=2).run(suite)
