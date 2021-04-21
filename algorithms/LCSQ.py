import algorithms.utils as utils
import numpy as np

def fill_matrix(s, t):
    M = np.zeros((len(s)+1, len(t)+1))
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            if s[i-1] == t[j-1]:
                M[i, j] = M[i - 1, j - 1] + 1
            else:
                M[i, j] = max(M[i, j - 1], M[i - 1, j])
    return M


def trace(s, t, M, i, j):
    if i == 0 or j == 0:
        return ''
    elif s[i-1] == t[j-1]:
        return trace(s, t, M, i - 1, j - 1) + s[i-1]
    elif M[i, j - 1] > M[i - 1, j]:
        return trace(s, t, M, i, j - 1)
    else:
        return trace(s, t, M, i - 1, j)


def main_LCSQ(fname):
    seqs = utils.read_fasta(fname)
    M = fill_matrix(seqs[0], seqs[1])
    subsequence = trace(seqs[0], seqs[1], M, len(seqs[0]), len(seqs[1]))
    return subsequence

if __name__ == '__main__':
    print(main_LCSQ('../datasets/LCSQ_1.txt'))  # pragma: no cover