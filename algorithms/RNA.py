def main_RNA(fname):
    """Transcribing DNA into RNA."""
    with open(fname, 'r') as f:
        dna = ''.join(f.read().strip())
    valid_dna = 'ACGT'
    if not (all(i in valid_dna for i in dna)):  # not a valid DNA
        raise Exception('Input Error')
    return dna.replace('T', 'U')  # replace T to U


if __name__ == '__main__':
    print(main_RNA('../datasets/RNA_3.txt'))  # pragma: no cover
