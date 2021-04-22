from algorithms.utils import read_fasta, BLOSUM62
import numpy as np
from colorama import Fore, Style
from algorithms.HAMM import HAMM
from algorithms.GAFF import add_leading_gaps, init_variables


def initializations(s, t, scoring_matrix, gap, gap_ext, conserved_seq, conserved_strength, bound,
                    ignore_start_gaps, auto_bound):
    """Initializations for the main function."""
    M, L, U, trace_M, trace_L, trace_U, row, col = init_variables(s, t)
    if auto_bound:
        bound = 10 + abs(len(s) - len(t))
    if ignore_start_gaps:
        M[1:, 0] = 0
        M[0, 1:] = 0
    else:
        # init beginning gap penalty
        M[1:, 0] = np.arange(gap, gap - M.shape[0] * abs(gap_ext) + abs(gap_ext), gap_ext)
        M[0, 1:] = np.arange(gap, gap - M.shape[1] * abs(gap_ext) + abs(gap_ext), gap_ext)
    if conserved_seq != "":
        for i in conserved_seq:
            scoring_matrix.loc[i, i] = conserved_strength
    return M, L, U, trace_M, trace_U, trace_L, row, col, bound


def get_aligned_seq_ext(s, t, L, U, M, trace_L, trace_U, trace_M, ignore_end_gaps):
    """Traceback best aligned two sequence using table information."""
    s_aligned, t_aligned = s, t
    L_max = np.max([np.max(L[-1, :]), np.max(L[-1, :])])
    U_max = np.max([np.max(U[-1, :]), np.max(U[-1, :])])
    M_max = np.max([np.max(M[-1, :]), np.max(M[-1, :])])
    scores = [L_max, U_max, M_max]
    trace = np.argmax(scores)
    i, j = len(s), len(t)
    # Build alignment via trace
    while i > 0 and j > 0:
        if ignore_end_gaps and j > np.argmax(M[-1, :]):  # add end gap to i
            j -= 1
            s_aligned = s_aligned[:i] + '-' + s_aligned[i:]
        elif ignore_end_gaps and i > np.argmax(M[:, -1]):  # add end gap to j
            i -= 1
            t_aligned = t_aligned[:j] + '-' + t_aligned[j:]
        else:
            if trace == 0:  # row
                if trace_L[i][j] == 0: trace = 2
                i -= 1
                t_aligned = t_aligned[:j] + '-' + t_aligned[j:]
            elif trace == 1:  # col
                if trace_U[i][j] == 0: trace = 2
                j -= 1
                s_aligned = s_aligned[:i] + '-' + s_aligned[i:]
            elif trace == 2:  # diagonal, no need to add
                if trace_M[i][j] == 1:
                    trace = 0
                elif trace_M[i][j] == 2:
                    trace = 1
                else:
                    i -= 1
                    j -= 1
    s_aligned, t_aligned = add_leading_gaps(t_aligned, s_aligned, i, j)
    return np.argmax(scores), s_aligned, t_aligned


def GAFF_extended(s, t, scoring_matrix, gap, gap_ext, conserved_seq="", conserved_strength=0, bound=-1,
                  ignore_start_gaps=False, ignore_end_gaps=False, auto_bound = False):
    """
    Global Alignment with Scoring Matrix and Affine Gap Penalty Extension.

    Inputs: Two protein strings s and t in FASTA format.
            conserved_seq: will increase the weight on the sequence.
            conserved_strength: weight on conserved_seq.
            bound: Define the range of bound dynamic programming. Negative number will run unbound version.
            auto_bound: Auto calculate the bound size using DNA length difference.
            ignore_start_gaps: ignoring start gaps in alignment, default False.
            ignore_end_gaps: ignoring end gaps in alignment, default False.

    Returns: The maximum alignment score between s and t, followed by two augmented strings
             s′ and t′ representing an optimal alignment of s and t.
    """
    M, L, U, trace_M, trace_U, trace_L, row, col, bound \
        = initializations(s, t, scoring_matrix, gap, gap_ext, conserved_seq,
                          conserved_strength, bound, ignore_start_gaps, auto_bound)
    # Build the table form top left
    if bound > 0:  # bound version
        for i in range(1, row):
            for j in range(max(1, i - bound), min(col, i + bound)):
                if j < i + bound:
                    costL = [M[i - 1, j] + gap, L[i - 1, j] + gap_ext]
                    L[i, j] = np.max(costL)
                    trace_L[i, j] = costL.index(L[i, j])
                if j > i - bound:
                    costU = [M[i, j - 1] + gap, U[i, j - 1] + gap_ext]
                    U[i, j] = np.max(costU)
                    trace_U[i, j] = costU.index(U[i, j])

                costM = [M[i - 1, j - 1] + scoring_matrix.loc[s[i - 1], t[j - 1]],
                         L[i, j], U[i, j]]
                M[i, j] = np.max(costM)
                trace_M[i, j] = costM.index(M[i, j])
    else:  # un-bound version
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

    return get_aligned_seq_ext(s, t, L, U, M, trace_L, trace_U, trace_M, ignore_end_gaps)


def print_seq_in_colour(s, t, scoring_matrix):
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


def print_all_info(s_aligned, t_aligned, max_score, scoring_matrix):
    """Print all sequence alignment information."""
    diffs = HAMM(s_aligned, t_aligned)
    new_s, new_t, num_of_gaps = print_seq_in_colour(s_aligned, t_aligned, scoring_matrix)
    print('Align score', max_score)
    print('Similarity:', len(s_aligned) - diffs, "/",
          len(s_aligned), ": ", round(diffs / len(s_aligned) * 100, 2), "%")
    print('Gaps:', num_of_gaps, "/", len(s_aligned), ": ", round(num_of_gaps / len(s_aligned) * 100, 2), "%")
    print(new_s)
    print(new_t)
    print(Style.RESET_ALL)


def main_extension(fname, scoring_matrix, gap, gap_ext, conserved_seq="", conserved_strength=0, bound=-1,
                   ignore_start_gaps=False, ignore_end_gaps=False, auto_bound = False):
    """Main function of modified GAFF algorithm."""
    s, t = read_fasta(fname)
    max_score, s_aligned, t_aligned = GAFF_extended(s, t, scoring_matrix, gap, gap_ext, conserved_seq,
                                                    conserved_strength, bound, ignore_start_gaps,
                                                    ignore_end_gaps, auto_bound)
    # show important information
    print_all_info(s_aligned, t_aligned, max_score, scoring_matrix)
    return max_score, s_aligned, t_aligned


if __name__ == '__main__':
    main_extension('../datasets/extension_5.txt', BLOSUM62(), -11, -1,
                   ignore_start_gaps=False, ignore_end_gaps=False, auto_bound=True)  # pragma: no cover
