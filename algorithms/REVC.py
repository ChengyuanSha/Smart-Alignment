def main_REVC(fname):
    with open(fname, 'r') as f:
        dna = ''.join(f.read().strip())
    if len(dna) <= 0 or len(dna) > 1000:
        raise Exception('Input Error')
    sequence_dic = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join([sequence_dic[b] for b in reversed(dna)])


if __name__ == '__main__':
    print(main_REVC('../datasets/REVC_2.txt'))  # pragma: no cover
