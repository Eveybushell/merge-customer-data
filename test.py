import unittest
from customerData import mergeData

class TestCustomerData (unittest.TestCase):
    def testSample1 (self):
        self.assertEqual(mergeData([101,104,107,0,0,0], [102,105,108],3,3),[101,102,104,105,107,108])

    def testSample2 (self):
            self.assertEqual(mergeData([103], [],1,0),[103])
    
    def testDataSet1Empty (self):
         self.assertEqual(mergeData([0], [103],0,1),[103])
    
    def testDataSetsEmpty (self):
         self.assertEqual(mergeData([0], [], 0, 0), "No customer data")
    
    def testWrongDataType (self):
         self.assertEqual(mergeData(15, [104, 105, 120], 1, 3), "Wrong data type")
    
    def testWrongListType (self):
         self.assertEqual(mergeData(['Billy', 'Tina', 'Zeke'], ['Alice', 'Emily', 'Fabien'], 3, 3), "Lists must have ints")

if __name__ == "__main__":
    unittest.main()