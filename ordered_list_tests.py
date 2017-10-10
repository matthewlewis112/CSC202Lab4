from ordered_list import *
import unittest

class test_Ordered_List(unittest.TestCase):
    #Tests represent functions
    def test_reper(self):
        oList = OrderedList()
        oList.add(12)
        oList.add(2)
        oList.add(35)
        oList.add(5)
        self.assertEqual(str(oList), "2, 5, 12, 35")
