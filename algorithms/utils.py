"""Common functions used by questions."""
import pandas as pd
import os
script_dir = os.path.dirname(__file__) # absolute dir the script is in


def read_fasta(fname):
    """Read in a Fasta file and returns a list of sequences."""
    temp = []
    seqs = []

    with open(fname, 'r') as f:
        for line in f.readlines():
            if line.startswith('>'):
                temp.append(line[1:].strip())
                seqs.append('')
            else:
                seqs[-1] += line.strip()
    # error checking
    for i in seqs:
        if not i.isalpha():
            raise Exception('Input Error')
    return seqs


def read_score_matrix(fname):
    """
    Read a score matrix like BLOSUM62.

    Read a text file of a scoring matrix.
    Return a score matrix dataframe with row and column as amino acids.
    """
    return pd.read_csv(fname, delimiter=r"\s+", header=0, index_col=0)


def BLOSUM62():
    """Return a BLOSUM62 score matrix dataframe."""
    rel_path = '../datasets/BLOSUM62.txt'
    abs_file_path = os.path.join(script_dir, rel_path)
    return read_score_matrix(abs_file_path)


if __name__ == '__main__':  # pragma: no cover
    test = BLOSUM62()  # pragma: no cover
    print(BLOSUM62())  # pragma: no cover
    print(BLOSUM62())  # pragma: no cover
