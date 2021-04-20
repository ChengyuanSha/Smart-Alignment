def read_input(fname):
    """Read txt file containing A DNA string."""
    with open(fname, 'r') as f:
        return f.read()


def main_SUBS(infile):
    seq, motif = infile.strip().split("\n")

    indices = []
    for n in range(len(seq)):
        if seq.startswith(motif, n):
            indices.append(n + 1)

    return indices


if __name__ == "__main__":
    infile = read_input("../datasets/SUBS_3.txt")
    print(main_SUBS(infile))
