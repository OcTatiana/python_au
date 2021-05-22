import unittest
from main import filter_list_of_dict
from main import string_to_dictionary


class TestDataAnalysis(unittest.TestCase):
    def test_string_to_dictionary(self):
        keys = ['data', 'resource', 'staff_id', 'count']
        line = '2020-04,1,1,38'

        result = string_to_dictionary(keys, line)
        expect = {'data': '2020-04', 'resource': '1', 'staff_id': '1', 'count': '38'}

        self.assertEqual(expect, result)

    def test_filter(self):
        list_of_dict = [{'source': '1', 'count': '2'},
                        {'source': '2', 'count': '2'},
                        {'source': '2', 'count': '1'}]
        key = 'source'
        value = '1'

        result = filter_list_of_dict(list_of_dict, key, value)
        expect = [{'source': '1', 'count': '2'}]

        self.assertEqual(expect, result)


if __name__ == '__main__':
    unittest.main()
