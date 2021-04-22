import numpy as np
import algorithms.utils as utils


def edit_distance(s, t):
    """

    Takes two protein strings s and t and returns the edit distance between them
    :param s: string1
    :param t: string2
    :return: Edit distance between s and t
    """
    m = len(s)
    n = len(t)
    M = np.zeros((m + 1, n + 1))
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                M[i, j] = j
            elif j == 0:
                M[i, j] = i
            elif s[i - 1] == t[j - 1]:
                M[i, j] = M[i - 1, j - 1]
            else:
                M[i, j] = 1 + min(M[i, j - 1],
                                  M[i - 1, j],
                                  M[i - 1, j - 1])
    return M[m, n]


def main_EDIT(fname):
    """

    Takes two protein strings in fasta format and returns the edit distance between the two
    :param fname: txt file in FASTA format
    :return:edit distance between the two strings
    """
    try:
        seqs = utils.read_fasta(fname)
    except IndexError:
        raise IndexError("File not in FASTA format")
    e_distance = edit_distance(seqs[0], seqs[1])
    return e_distance


if __name__ == '__main__':
    print(main_EDIT('../datasets/EDIT_2.txt'))  # pragma: no cover
