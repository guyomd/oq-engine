import unittest
import numpy
from openquake.commonlib.datastore import DataStore


class DataStoreTestCase(unittest.TestCase):
    def setUp(self):
        self.dstore = DataStore()

    def test_pik(self):
        # store pickleable Python objects
        self.dstore['key1'] = 'value1'
        self.assertEqual(len(self.dstore), 1)
        self.dstore['key2'] = 'value2'
        self.assertEqual(list(self.dstore), 'key1 key2'.split())
        del self.dstore['key2']
        self.assertEqual(list(self.dstore), ['key1'])
        self.assertEqual(self.dstore['key1'], 'value1')
        self.dstore.remove()

    def test_hdf5(self):
        # store numpy arrays as hdf5 files
        with self.assertRaises(ValueError):
            self.dstore['key1_h5'] = 'value1'
        self.assertEqual(len(self.dstore), 0)
        self.dstore['key1_h5'] = value1 = numpy.array(['a', 'b'])
        self.dstore['key2_h5'] = numpy.array([1, 2])
        self.assertEqual(list(self.dstore), 'key1_h5 key2_h5'.split())
        del self.dstore['key2_h5']
        self.assertEqual(list(self.dstore), ['key1_h5'])
        numpy.testing.assert_equal(self.dstore['key1_h5'], value1)
        self.dstore.remove()
