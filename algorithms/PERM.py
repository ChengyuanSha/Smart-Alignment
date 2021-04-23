def main_PERM(fname):
    """

    Takes an integer n and returns all permutations of integers 1 to n, and the number of permutations
    :param fname: txt file with an integer >1 in it
    :return: all permutations of the list of integers from 1 to n
    """
    with open(fname, 'r') as f:
        number = f.readline()
    number = int(number)
    numbers = []
    for i in range(1, number + 1):
        numbers.append(i)
    perm = permutations(numbers)
    perm.insert(0, len(perm))
    return perm


def permutations(numbers):
    """

    Takes a list of integers and returns all permutations of integers 1 to n
    :param numbers:list of integers from 1 to n
    :return:all permutations of list of integers 1 to n
    """
    if len(numbers) == 0:
        return []  # pragma: no cover
    if len(numbers) == 1:
        return [numbers]
    perm = []
    for i in range(len(numbers)):
        first = numbers[i]
        rest = numbers[:i] + numbers[i + 1:]
        for j in permutations(rest):
            perm.append([first] + j)
    return perm


if __name__ == '__main__':
    print(main_PERM('../datasets/PERM_1.txt'))  # pragma: no cover
