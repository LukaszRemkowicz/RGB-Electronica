import unittest
from scanner import find_corect_document


def write_to_file(document):
    """ Write to file helper function """

    open('test_scanner.txt', 'w').close()
    with open('test_scanner.txt', 'w') as f:
        f.write(document)


class TestScanner(unittest.TestCase):
    """ Test scanner function """

    def test_one_document(self):
        """ Test one document  """

        document = 'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\nbyr:1937 iyr:2017 cid:147 hgt:183cm'
        expected_result = 1

        write_to_file(document)
        result = find_corect_document('test_scanner.txt')

        self.assertEqual(expected_result, result)

    def test_missing_value(self):
        """Testing wrong documment"""

        document = 'eyr:2029 iyr:\nhcl:#ceb3a1 byr:1939 ecl:blu\nhgt:163cm\npid:660456119'
        expected_result = 0

        write_to_file(document)
        result = find_corect_document('test_scanner.txt')

        self.assertEqual(expected_result, result)

    def test_two_documents(self):
        """Testing two documments"""

        document = 'eyr:2029 iyr:\nhcl:#ceb3a1 byr:1939 ecl:blu\nhgt:163cm\npid:660456119\n\n' \
                   'hcl:#0f8b2e ecl:grn\nbyr:1975 iyr:2011\neyr:2028 cid:207 hgt:158cm\npid:755567813'
        expected_result = 1

        write_to_file(document)
        result = find_corect_document('test_scanner.txt')

        self.assertEqual(expected_result, result)

    def test_wrong_document(self):
        """ Testing slitted by empty line document"""

        document = 'eyr:2029 iyr:\nhcl:#ceb3a1 byr:1939 ecl:blu\n\nhgt:163cm\npid:660456119'
        expected_result = 0

        write_to_file(document)
        result = find_corect_document('test_scanner.txt')

        self.assertEqual(expected_result, result)
