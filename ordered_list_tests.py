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
    def test_add(self):
        pass
    def test_remove(self):
        pass
    def test_search_forward(self):
        pass
    def test_search_backward(self):
        oList = OrderedList()
        oList.add(1)
        oList.add(2)
        oList.add(3)
        oList.add(4)
        oList.add(5)
        self.assertTrue(oList.search_backward(1))
        self.assertTrue(oList.search_backward(2))
        self.assertTrue(oList.search_backward(3))
        self.assertTrue(oList.search_backward(4))
        self.assertTrue(oList.search_backward(5))
        self.assertFalse(oList.search_backward(12))
    def test_is_empty(self):
        oList = OrderedList()
        self.assertTrue(oList.is_empty())
        oList.add(1)
        self.assertFalse(oList.is_empty())
    def test_size(self):
        oList = OrderedList()
        self.assertEqual(oList.size(), 0)
        oList.add(5)
        oList.add(7)
        self.assertEqual(oList.size(), 2)
    def test_index(self):
        oList = OrderedList()
        self.assertEqual(oList.index(12), None)
        oList.add(12)
        self.assertEqual(oList.index(12), 0)
    def test_pop(self):
        pass
if __name__ == '__main__':
    unittest.main()
