from algorithms.utils import read_fasta, BLOSUM62
import numpy as np


def main_GCON(s, t, BLOSUM62, gap):
    '''
    Inputs: Two protein strings s and t in FASTA format.
    Return: The maximum alignment score between s and t using BLOSUM62 scoring matrix
    and a constant gap penalty equal to 5.
    '''
    table = np.zeros((len(s) + 1, len(t) + 1), dtype=int)
    X = np.full((len(s) + 1, len(t) + 1), np.NINF, dtype=int)
    Y = np.full((len(s) + 1, len(t) + 1), np.NINF, dtype=int)
    # setting constant gap penalty
    table[1:, 0] = gap
    table[0, 1:] = gap

    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            # row horizontal
            X[i][j] = max([table[i - 1][j] + gap, X[i - 1][j]])
            # column vertical
            Y[i][j] = max([table[i][j - 1] + gap, Y[i][j - 1]])
            # diagonal
            table[i][j] = max([table[i - 1][j - 1] + BLOSUM62.loc[s[i - 1], t[j - 1]],
                               X[i][j], Y[i][j]])
    # bottom-right corner of the table is the max score.
    return table[-1][-1]


if __name__ == '__main__':  # pragma: no cover
    s, t = read_fasta('../datasets/GCON_1.txt')  # pragma: no cover
    max_score = main_GCON(s, t, BLOSUM62(), -5)  # pragma: no cover
    print(max_score)  # pragma: no cover
