import algorithms.utils as utils
import numpy as np


def fill_matrix(s, t):
    """

    Takes two strings and scores the length of the longest common subsequence at each index
    :param s:string1
    :param t:string2
    :return:Matrix where the score at each index M(i,j) is the length of the longest common subsequence at s(i) and t(j)
    """
    M = np.zeros((len(s) + 1, len(t) + 1))
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i - 1] == t[j - 1]:
                M[i, j] = M[i - 1, j - 1] + 1
            else:
                M[i, j] = max(M[i, j - 1], M[i - 1, j])
    return M


def trace(s, t, M, i, j):
    """

    Trace a matrix filled with the values of longest subsequence where M(i,j) is score between s(i), t(j)
    :param s: string1
    :param t: string2
    :param M: Matrix subsequence length at each input
    :param i: length of string1
    :param j: length of string2
    :return: Longest common subsequence
    """
    if i == 0 or j == 0:
        return ''
    elif s[i - 1] == t[j - 1]:
        return trace(s, t, M, i - 1, j - 1) + s[i - 1]
    elif M[i, j - 1] > M[i - 1, j]:
        return trace(s, t, M, i, j - 1)
    else:
        return trace(s, t, M, i - 1, j)


def main_LCSQ(fname):
    """

    returns the longest common subsequence of two strings from a .txt file in FASTA format
    :param fname: .txt file in FASTA format
    :return:Longest common subsequence
    """
    try:
        seqs = utils.read_fasta(fname)
    except IndexError:
        raise IndexError("File not in FASTA format")
    M = fill_matrix(seqs[0], seqs[1])
    subsequence = trace(seqs[0], seqs[1], M, len(seqs[0]), len(seqs[1]))
    return subsequence


if __name__ == '__main__':
    print(main_LCSQ('../datasets/LCSQ_1.txt'))  # pragma: no cover
