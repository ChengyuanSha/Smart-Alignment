from algorithms.utils import read_fasta, BLOSUM62
import numpy as np

def main_GCON(s, t, BLOSUM62, gap):
    """Global Alignment with Constant Gap Penalty.

    Inputs: Two protein strings s and t in FASTA format.
    Return: The maximum alignment score between s and t using BLOSUM62 scoring matrix
    and a constant gap penalty equal to 5.
    """
    neg_infinity = -999999
    M = np.zeros((len(s) + 1, len(t) + 1), dtype=int) # middle scores
    L = np.full((len(s) + 1, len(t) + 1), neg_infinity, dtype=int) # lower scores
    U = np.full((len(s) + 1, len(t) + 1), neg_infinity, dtype=int) # upper scores
    # setting constant gap penalty
    M[1:, 0] = gap
    M[0, 1:] = gap

    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            # row horizontal
            L[i][j] = max([M[i - 1][j] + gap, L[i - 1][j]])
            # column vertical
            U[i][j] = max([M[i][j - 1] + gap, U[i][j - 1]])
            # diagonal
            M[i][j] = max([M[i - 1][j - 1] + BLOSUM62.loc[s[i - 1], t[j - 1]],
                               L[i][j], U[i][j]])
    # bottom-right corner of the M is the max score.
    return M[-1][-1]


if __name__ == '__main__':  # pragma: no cover
    s, t = read_fasta('../datasets/GCON_1.txt')  # pragma: no cover
    max_score = main_GCON(s, t, BLOSUM62(), -5)  # pragma: no cover
    print(max_score)  # pragma: no cover
