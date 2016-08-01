from mock import patch
import unittest
import name_getter

class TestNameGetter(unittest.TestCase):

    def test_get_alice(self):
        name_getter.raw_input = lambda _: 'Alice'

        ng = name_getter.NameGetter()
        ng.get_name()
        self.assertEquals(ng.name, 'Alice')


if __name__ == '__main__':
    unittest.main()