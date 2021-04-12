def read_input(fname):
    """Read txt file containing A DNA string."""
    with open(fname, 'r') as f:
        return f.read()


def main_DNA(dna):
    """Counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in dna."""
    if len(dna) > 1000 or len(dna) <= 0:
        raise Exception('Input Error')
    dna_counts = map(dna.count, ['A', 'C', 'G', 'T'])
    return ' '.join(map(str, dna_counts))


if __name__ == '__main__':
    dna = read_input('../datasets/DNA_1.txt')  # pragma: no cover
    print(main_DNA(dna))  # pragma: no cover
