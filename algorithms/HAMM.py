def read_input(fname):
    """Read txt file containing two DNA strings."""
    with open(fname, 'r') as f:
        dna1, dna2 = f.read().split('\n')
    return dna1, dna2

def HAMM(dna1, dna2):
    """Not bounded by DNA length version."""
    return sum(c1 != c2 for c1, c2 in zip(dna1, dna2))


def main_HAMM(dna1, dna2):
    """Counting number of point Mutations between two DNA."""
    if len(dna1) <= 0 or len(dna1) > 1000 or len(dna2) <= 0 or len(dna2) > 1000:
        raise Exception('Input Error')
    return HAMM(dna1, dna2)


if __name__ == '__main__':
    dna1, dna2 = read_input('../datasets/HAMM_1.txt')  # pragma: no cover
    print(main_HAMM(dna1, dna2))  # pragma: no cover
