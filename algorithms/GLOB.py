from algorithms.utils import read_fasta, BLOSUM62
import numpy as np


def score(s, t, g, scoring_matrix):
    """

    Takes two protein strings, s and t, a gap penalty, and a scoring matrix and returns the maximum score of the
    global alignment of the two strings.
    :param s: string1
    :param t: string2
    :param g: gap penalty
    :param scoring_matrix: scoring matrix
    :return: Maximum score of alignment
    """
    m = len(s)
    n = len(t)
    M = np.zeros((m + 1, n + 1))
    try:
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    M[i, j] = j * -g
                elif j == 0:
                    M[i, j] = i * -g
                else:
                    M[i, j] = max(M[i, j - 1] - g,
                                  M[i - 1, j] - g,
                                  M[i - 1, j - 1] + scoring_matrix.loc[s[i - 1], t[j - 1]])
    except KeyError:
        raise KeyError("Invalid Amino Acid Code")
    return M[m, n]


def main_GLOB(fname):
    """

    Takes two protein strings from a .txt in FASTA format and returns the length of the maximum scoring global
    alignment using BLOSUM62 matrix and a gap penalty of 5.
    :param fname: .txt file in FASTA format
    :return: maximum score of the global alignment
    """
    seqs = read_fasta(fname)
    max_score = score(seqs[0], seqs[1], 5, BLOSUM62())
    return max_score


if __name__ == '__main__':
    print(main_GLOB('../datasets/GLOB_1.txt'))  # pragma: no cover
