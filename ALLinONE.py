import unittest
from A import A
from B import B
class ALLinONE(unittest.TestCase):
    if __name__ == '__main__':
        loader = unittest.TestLoader()
        module1 = A.suite()
        module2 = A.suite()
        # module2 = ChatTest_TicketQuerying.suite()
        # module3 = ChatTest_MultilingualHindi.suite()
        suite = unittest.TestSuite([module1, module2])
        unittest.TextTestRunner(verbosity=2).run(suite
