import unittest


class B(unittest.TestCase):
    def test_valid2(self):
        self.assertEqual(1,1)
    def test_valid3(self):
        self.assertEqual(2,2)

    @staticmethod
    def suite():
        suite = unittest.TestLoader().loadTestsFromTestCase(B)
        unittest.TextTestRunner(verbosity=2).run(suite)
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(B)
    unittest.TextTestRunner(verbosity=2).run(suite)
