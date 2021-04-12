def read_input(fname):
    """Read txt file containing A DNA string."""
    with open(fname, 'r') as f:
        return ''.join(f.read().strip())


def main_RNA(dna):
    """Transcribing DNA into RNA."""
    valid_dna = 'ACGT'
    if not (all(i in valid_dna for i in dna)):  # not a valid DNA
        raise Exception('Input Error')
    return dna.replace('T', 'U')  # replace T to U


if __name__ == '__main__':
    dna = read_input('../datasets/RNA_1.txt')  # pragma: no cover
    print(main_RNA(dna))  # pragma: no cover
