import re


def find_corect_document(file):
    result = []

    with open(file, 'r') as f:
        lines = f.read()

        split_lines = lines.split('\n\n')

        for scanner in split_lines:
            split_document = re.split(' |\n', scanner)

            line = {key: value for key, value in [el.split(':') for el in split_document]}

            try:
                is_empty = [
                    True if line['byr'] else False,
                    True if line['iyr'] else False,
                    True if line['eyr'] else False,
                    True if line['hgt'] else False,
                    True if line['hcl'] else False,
                    True if line['ecl'] else False,
                    True if line['pid'] else False
                ]
                result.append(all(is_empty))

            except KeyError:
                pass

    result = [element for element in result if element is True]

    return len(result)


if __name__ == "__main__":
    print(find_corect_document('zad2.txt'))
