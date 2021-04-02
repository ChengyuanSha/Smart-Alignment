def read_input(fname):
    """Read txt file containing A DNA string."""
    with open(fname, 'r') as f:
        return f.read()


def main_DNA(fname):
    """Counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in dna."""
    dna = read_input(fname)
    if len(dna) > 1000 or len(dna) <= 0:
        raise Exception('Input Error')
    dna_counts = map(dna.count, ['A', 'C', 'G', 'T'])
    return ' '.join(map(str, dna_counts))


if __name__ == '__main__':
    print(main_DNA('../datasets/DNA_1.txt')) # pragma: no cover
