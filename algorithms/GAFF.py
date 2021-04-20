from algorithms.utils import read_fasta, BLOSUM62
import numpy as np


def get_aligned_seq(s, t, L, U, M, trace_L, trace_U, trace_M):
    """Traceback best aligned two sequence using table information."""
    s_aligned, t_aligned = s, t
    scores = [L[-1, -1], U[-1, -1], M[-1, -1]]
    trace = np.argmax(scores)
    i, j = len(s), len(t)
    # Build alignment via trace
    while i > 0 and j > 0:
        if trace == 0:
            if trace_L[i, j] == 0: trace = 2
            i -= 1
            t_aligned = t_aligned[:j] + '-' + t_aligned[j:]
        elif trace == 1:
            if trace_U[i, j] == 0: trace = 2
            j -= 1
            s_aligned = s_aligned[:i] + '-' + s_aligned[i:]
        elif trace == 2:
            if trace_M[i, j] == 1:
                trace = 0
            elif trace_M[i, j] == 2:
                trace = 1
            else:
                i -= 1
                j -= 1
    # check the leading gaps
    for _ in range(i):
        t_aligned = t_aligned[:0] + '-' + t_aligned[0:]
    for _ in range(j):
        s_aligned = s_aligned[:0] + '-' + s_aligned[0:]
    return np.amax(scores), s_aligned, t_aligned


def main_GAFF(s, t, scoring_matrix, gap, gap_ext):
    """
    Global Alignment with Scoring Matrix and Affine Gap Penalty.

    Inputs: Two protein strings s and t in FASTA format.
    Returns: The maximum alignment score between s and t, followed by two augmented strings
    s′ and t′ representing an optimal alignment of s and t.
    """
    # initializations
    neg_infinity = -999999
    row, col = len(s) + 1, len(t) + 1
    M = np.zeros((row, col), dtype=int)  # main table
    L = np.full((row, col), neg_infinity, dtype=int)  # lower scores
    U = np.full((row, col), neg_infinity, dtype=int)  # upper scores
    trace_M = np.zeros((row, col), dtype=int)
    trace_L = np.zeros((row, col), dtype=int)
    trace_U = np.zeros((row, col), dtype=int)
    # init beginning gap penalty
    M[1:, 0] = np.arange(gap, gap - M.shape[0] * abs(gap_ext) + abs(gap_ext), gap_ext)
    M[0, 1:] = np.arange(gap, gap - M.shape[1] * abs(gap_ext) + abs(gap_ext), gap_ext)
    # Build the table form top left
    for i in range(1, row):
        for j in range(1, col):
            costL = [M[i - 1, j] + gap, L[i - 1, j] + gap_ext]
            L[i, j] = np.max(costL)
            trace_L[i, j] = costL.index(L[i, j])

            costU = [M[i, j - 1] + gap, U[i, j - 1] + gap_ext]
            U[i, j] = np.max(costU)
            trace_U[i, j] = costU.index(U[i, j])

            costM = [M[i - 1, j - 1] + scoring_matrix.loc[s[i - 1], t[j - 1]],
                     L[i, j], U[i, j]]
            M[i, j] = np.max(costM)
            trace_M[i, j] = costM.index(M[i, j])
    return get_aligned_seq(s, t, L, U, M, trace_L, trace_U, trace_M)


if __name__ == '__main__':
    s, t = read_fasta('../datasets/GAFF_2.txt')  # pragma: no cover
    alignment = main_GAFF(s, t, BLOSUM62(), -11, -2)  # pragma: no cover
    print('\n'.join(map(str, alignment)))  # pragma: no cover
