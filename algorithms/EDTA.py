from utils import read_fasta


def main_EDTA(seqs):
    s, t = seqs

    # Initialize the distance and traceback matrices with zeros.
    d = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]
    traceback = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]

    # Each cell in the first row and column recieves a gap penalty (-1).
    for i in range(1, len(s) + 1):
        d[i][0] = i
    for j in range(1, len(t) + 1):
        d[0][j] = j

    # Fill in the distance and traceback matrices.
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            scores = [d[i - 1][j - 1] + (s[i - 1] != t[j - 1]),  # 0 = match
                      d[i - 1][j] + 1,  # 1 = insertion
                      d[i][j - 1] + 1]  # 2 = deletion
            d[i][j] = min(scores)
            traceback[i][j] = scores.index(d[i][j])

    # The edit distance the last cell (bottom-right) of the distance matrix.
    edit_dist = d[-1][-1]

    # Initialize the aligned strings as the input strings.
    s_align, t_align = s, t

    # traceback to the edge of the matrix starting at the bottom right.
    i, j = len(s), len(t)

    while i > 0 and j > 0:
        if traceback[i][j] == 1:
            i -= 1
            t_align = t_align[:j] + '-' + t_align[j:]
        elif traceback[i][j] == 2:
            j -= 1
            s_align = s_align[:i] + '-' + s_align[i:]
        else:
            i -= 1
            j -= 1

    # Prepend insertions/deletions if necessary.
    for dash in range(i):
        t_align = t_align[:0] + '-' + t_align[0:]
    for dash in range(j):
        s_align = s_align[:0] + '-' + s_align[0:]

    return edit_dist, s_align, t_align


if __name__ == '__main__':
    seqs = read_fasta("../datasets/EDTA_3.txt")
    print(main_EDTA(seqs))
