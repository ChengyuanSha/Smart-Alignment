def read_input(fname):
    """Read txt file containing a DNA string."""
    with open(fname, 'r') as f:
        return ''.join(f.read().strip())


def main_REVC(dna):
    """Find complementing a strand of DNA."""
    if len(dna) <= 0 or len(dna) > 1000:
        raise Exception('Input Error')
    sequence_dic = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join([sequence_dic[b] for b in reversed(dna)])


if __name__ == '__main__':
    dna = read_input('../datasets/REVC_2.txt')  # pragma: no cover
    print(main_REVC(dna))  # pragma: no cover
