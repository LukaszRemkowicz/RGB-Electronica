import unittest
from find_len import itterate_over_range
import random


def read_lines(element):
    """ Check line helper function """

    if list(element) == sorted(list(element)):
        if '11' in element or \
                '22' in element or \
                '33' in element or \
                '44' in element or \
                '55' in element or \
                '66' in element or \
                '77' in element or \
                '88' in element or \
                '99':
            return True
    else:
        return False


class TestSafe(unittest.TestCase):
    """ Test length of list with numbers which fits requirements """

    def test_small_range(self):
        """ Test small range """

        start = 110
        stop = 122
        expected_result = 10

        result = itterate_over_range(start, stop, 'test_file.txt')

        self.assertEqual(expected_result, result)

    def test_check_result(self):
        """ Test if written numbers to file, fits requirements """

        start = 114112
        stop = 365579

        itterate_over_range(start, stop, 'test_file.txt')

        result = []
        with open('test_file.txt', 'r') as f:
            lines = f.read()
            for line in lines:
                result.append(read_lines(line))

        result = all(result)
        self.assertTrue(result)

    def test_random(self):
        """ Get random number and check requirements """

        start = 114112
        stop = 365579

        itterate_over_range(start, stop, 'test_file.txt')

        with open('test_file.txt', 'r') as f:
            lines = f.read()
            lines = lines.split('\n')

            get_random = random.choices(lines)
            result = read_lines(get_random)

            self.assertTrue(result)

