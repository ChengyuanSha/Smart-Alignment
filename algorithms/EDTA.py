from algorithms.utils import read_fasta


def create_gap_from_distmat(matrix, s, t):
    """Creates gapped strings based on distance matrix."""

    gapped_s, gapped_t = '', ''
    i, j = len(s), len(t)

    while (i > 0 and j > 0):
        left = matrix[i][j - 1]
        up = matrix[i - 1][j]
        diag = matrix[i - 1][j - 1]
        best = min(left, up, diag)
        if matrix[i][j] == best:
            # match
            gapped_s = s[i - 1] + gapped_s
            gapped_t = t[j - 1] + gapped_t
            i -= 1
            j -= 1
        elif (best == left and best == up) or (best != left and best != up):
            # mismatch
            gapped_s = s[i - 1] + gapped_s
            gapped_t = t[j - 1] + gapped_t
            i -= 1
            j -= 1
        elif best != left and best == up:
            # gap in second string
            gapped_s = s[i - 1] + gapped_s
            gapped_t = '-' + gapped_t
            i -= 1
        elif best == left and best != up:
            # gap in first string
            gapped_s = '-' + gapped_s
            gapped_t = t[j - 1] + gapped_t
            j -= 1
        else:
            print('shouldnt get here') # pragma: no cover
            return 0 # pragma: no cover
    return gapped_s, gapped_t


def main_EDTA(seqs):
    '''
    Given: Two strings s and t in FASTA format.
    Return: The edit distance dE(s,t) followed by two gapped strings s′ and t′ representing an optimal alignment.
    '''

    s, t = seqs
    len_one, len_two = len(s), len(t)

    # initialize distance matrix with zeroes
    dist_mat = [[0] * (len_two + 1) for _ in range(len_one + 1)]
    # fill distance matrix with values
    for i in range(len_one + 1):
        dist_mat[i][0] = i
    for j in range(len_two + 1):
        dist_mat[0][j] = j
    for i in range(1, len_one + 1):
        for j in range(1, len_two + 1):
            left = dist_mat[i - 1][j] + 1
            up = dist_mat[i][j - 1] + 1
            diag = dist_mat[i - 1][j - 1]
            if s[i - 1] != t[j - 1]:
                diag += 1
            dist_mat[i][j] = min(left, up, diag)

    # edit distance is bottom right value of distance matrix
    dist = dist_mat[len_one][len_two]

    gapped_s, gapped_t = create_gap_from_distmat(dist_mat, s, t)

    return (dist, gapped_s, gapped_t)


if __name__ == '__main__':
    seqs = read_fasta("../datasets/EDTA_1.txt") # pragma: no cover
    print(main_EDTA(seqs)) # pragma: no cover
