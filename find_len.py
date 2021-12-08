def check_string(string, file):
    """ check if there is doubled number and if numbers are increasing
    Optional: writing result to file """

    flag = False
    for element_a, element_b in zip(string[:-1], string[1:]):
        if element_a > element_b:
            return False
        if element_a == element_b:
            flag = True

            # Optional
            open(file, 'a').close()
            with open(file, 'a') as f:
                f.write(f'{string}\n')
    return flag


def itterate_over_range(start, stop, file):
    """ itterate over given range to see, if number fits requirements """

    return len([element for element in range(start, stop + 1) if check_string(str(element), file)])


if __name__ == '__main__':
    print(itterate_over_range(265275, 781584, 'result.txt'))
