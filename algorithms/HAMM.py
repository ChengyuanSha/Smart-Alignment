def main_HAMM(fname):
    """Counting Point Mutations between two DNA."""
    with open(fname, 'r') as f:
        dna1, dna2 = f.read().split('\n')
    if len(dna1) <= 0 or len(dna1) > 1000 or len(dna2) <= 0 or len(dna2) > 1000:
        raise Exception('Input Error')
    return sum(c1 != c2 for c1, c2 in zip(dna1, dna2))


if __name__ == '__main__':
    print(main_HAMM('../datasets/HAMM_3.txt'))  # pragma: no cover
