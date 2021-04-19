from algorithms.utils import read_fasta, BLOSUM62
import numpy as np
from colorama import Fore, Style
from algorithms.GAFF import main_GAFF, get_aligned_seq
from algorithms.HAMM import main_HAMM


def initializations(s, t, scoring_matrix, gap, gap_ext, conserved_seq, conserved_strength,
                    ignore_start_gaps, ignore_end_gaps):
    """Initializations for the main function."""
    neg_infinity = -999999
    row, col = len(s) + 1, len(t) + 1
    M = np.zeros((row, col), dtype=int)  # middle scores
    L = np.full((row, col), neg_infinity, dtype=int)  # lower scores
    U = np.full((row, col), neg_infinity, dtype=int)  # upper scores
    trace_M = np.zeros((row, col), dtype=int)
    trace_L = np.zeros((row, col), dtype=int)
    trace_U = np.zeros((row, col), dtype=int)
    if ignore_start_gaps and ignore_end_gaps:
        M[1:, 0] = 0
        M[0, 1:] = 0
    elif ignore_start_gaps and not ignore_end_gaps:
        M[1:, 0] = 0
        M[0, 1:] = np.arange(gap, gap - M.shape[1] + 1, gap_ext)  # init gap penalty
    elif not ignore_start_gaps and ignore_end_gaps:
        M[1:, 0] = np.arange(gap, gap - M.shape[0] + 1, gap_ext)
        M[0, 1:] = 0
    else:
        M[1:, 0] = np.arange(gap, gap - M.shape[0] + 1, gap_ext)  # init gap penalty
        M[0, 1:] = np.arange(gap, gap - M.shape[1] + 1, gap_ext)  # init gap penalty
    last_i, last_j = 0, 0
    for i in conserved_seq:
        scoring_matrix.loc[i, i] = conserved_strength
    return M, L, U, trace_M, trace_U, trace_L, last_i, last_j, row, col


def GAFF_extended(s, t, scoring_matrix, gap, gap_ext, conserved_seq, conserved_strength,
                  ignore_start_gaps, ignore_end_gaps):
    """
    Global Alignment with Scoring Matrix and Affine Gap Penalty Extension.

    Inputs: Two protein strings s and t in FASTA format.
    Returns: The maximum alignment score between s and t, followed by two augmented strings
    s′ and t′ representing an optimal alignment of s and t.
    """
    M, L, U, trace_M, trace_U, trace_L, last_i, last_j, row, col \
        = initializations(s, t, scoring_matrix, gap, gap_ext, conserved_seq,
                          conserved_strength, ignore_start_gaps, ignore_end_gaps)
    # Build the table form top left
    for i in range(1, row):
        for j in range(1, col):
            costX = [M[i - 1][j] + gap, L[i - 1][j] + gap_ext]
            L[i][j] = max(costX)
            trace_L[i][j] = costX.index(L[i][j])

            costY = [M[i][j - 1] + gap, U[i][j - 1] + gap_ext]
            U[i][j] = max(costY)
            trace_U[i][j] = costY.index(U[i][j])

            costM = [M[i - 1][j - 1] + scoring_matrix.loc[s[i - 1], t[j - 1]],
                     L[i][j], U[i][j]]
            M[i][j] = max(costM)
            trace_M[i][j] = costM.index(M[i][j])
            last_i, last_j = i, j
    return get_aligned_seq(s, t, L, U, M, trace_L, trace_U, trace_M, last_i, last_j)


def print_in_colour(s, t, scoring_matrix):
    """Print sequence alignment in colour for better visualization."""
    new_s = ""
    new_t = ""
    num_of_gaps = 0
    for i, _ in enumerate(s):
        if s[i] == '-' or t[i] == '-':  # gaps
            new_s += (Fore.CYAN + s[i])
            new_t += (Fore.CYAN + t[i])
            num_of_gaps += 1
        elif scoring_matrix.loc[s[i], t[i]] >= 0:  # good alignment
            new_s += (Fore.LIGHTGREEN_EX + s[i])
            new_t += (Fore.LIGHTGREEN_EX + t[i])
        elif scoring_matrix.loc[s[i], t[i]] < 0:  # bad alignment
            new_s += (Fore.LIGHTRED_EX + s[i])
            new_t += (Fore.LIGHTRED_EX + t[i])
    return new_s, new_t, num_of_gaps


def main_extension(fname, conserved_seq, conserved_strength, scoring_matrix, gap, gap_ext,
                   ignore_start_gaps=False, ignore_end_gaps=False):
    """Modified GAFF algorithm."""
    s, t = read_fasta(fname)
    max_score, s_aligned, t_aligned = GAFF_extended(s, t, scoring_matrix, gap, gap_ext, conserved_seq,
                                                    conserved_strength, ignore_start_gaps, ignore_end_gaps)
    # show important information
    diffs = main_HAMM(s_aligned, t_aligned)
    new_s, new_t, num_of_gaps = print_in_colour(s_aligned, t_aligned, scoring_matrix)
    print('Align score', max_score)
    print('Similarity:', len(s_aligned) - diffs, "/", len(s_aligned), ": ", round(diffs / len(s_aligned) * 100, 2), "%")
    print('Gaps:', num_of_gaps, "/", len(s_aligned), ": ", round(num_of_gaps / len(s_aligned) * 100, 2), "%")
    print(new_s)
    print(new_t)
    print(Style.RESET_ALL)
    print()


def experiment1():
    """Compare our extended algorithm VS original algorithm."""
    print("Extended Global Sequence Alignment:")
    print("Scoring matrix used: BLOSUM62.")
    main_extension('../datasets/extension_1.txt', 'STAY', 30, BLOSUM62(), -11, -1)
    # original GAFF
    print("Original Global Sequence Alignment:")
    print("Scoring matrix used: BLOSUM62.")
    s, t = read_fasta('../datasets/extension_1.txt')  # pragma: no cover
    max_score, s_aligned, t_aligned = main_GAFF(s, t, BLOSUM62(), -11, -1)  # pragma: no cover
    print('Align score', max_score)
    new_s, new_t, num_of_gaps = print_in_colour(s_aligned, t_aligned, BLOSUM62())
    diffs = main_HAMM(s_aligned, t_aligned)
    print('Align score', max_score)
    print('Similarity:', len(s_aligned) - diffs, "/", len(s_aligned), ": ", round(diffs / len(s_aligned) * 100, 2), "%")
    print('Gaps:', num_of_gaps, "/", len(s_aligned), ": ", round(num_of_gaps / len(s_aligned) * 100, 2), "%")
    print(new_s)
    print(new_t)


def experiment2():
    """Semi-global alignment experiment."""
    # Original alignment
    main_extension('../datasets/extension_2.txt', 'STAY', 30, BLOSUM62(), -15, -1,
                   ignore_start_gaps=False, ignore_end_gaps=False)
    # Semi-global alignment
    main_extension('../datasets/extension_2.txt', 'STAY', 30, BLOSUM62(), -8, -1,
                   ignore_start_gaps=True, ignore_end_gaps=True)


if __name__ == '__main__':
    # experiment1()
    experiment2()
