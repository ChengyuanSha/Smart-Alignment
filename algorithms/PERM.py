def main_PERM(fname):
    with open(fname, 'r') as f:
        number = f.readline()
    number = int(number)
    numbers = []
    for i in range(1, number + 1):
        numbers.append(i)
    return permutations(numbers)


def permutations(numbers):
    if len(numbers) == 0:
        return []
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
