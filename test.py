import unittest
from customerData import mergeData

class MergeTest (unittest.TestCase):
    
    def sampleTest1 (self):
        self.assertEqual(mergeData([101,104,107,0,0,0], [102,105,108], 3, 3), [101,102,104,105,107,108])

if __name__ == "__main__":
    unittest.main()