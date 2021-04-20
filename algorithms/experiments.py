from GAFF_extension import main_extension, print_all_info
from utils import BLOSUM62, read_fasta
from GAFF import main_GAFF


def experiment1():
    """Conserved sequence experiment."""
    print("Extended Global Sequence Alignment:")
    print("Scoring matrix used: BLOSUM62.")
    main_extension('../datasets/extension_1.txt', BLOSUM62(), -11, -1,
                   conserved_seq='STAY', conserved_strength=30)
    # Comparison with original GAFF algorithm
    print("Original Global Sequence Alignment:")
    print("Scoring matrix used: BLOSUM62.")
    s, t = read_fasta('../datasets/extension_1.txt')
    max_score, s_aligned, t_aligned = main_GAFF(s, t, BLOSUM62(), -11, -1)
    print_all_info(s_aligned, t_aligned, max_score, BLOSUM62())


def experiment2():
    """Semi-global alignment experiment."""
    # Semi-global alignment
    main_extension('../datasets/extension_2.txt', BLOSUM62(), -15, -2,
                   ignore_start_gaps=True, ignore_end_gaps=True)
    # Comparison with original GAFF algorithm
    main_extension('../datasets/extension_2.txt', BLOSUM62(), -15, -2,
                   ignore_start_gaps=False, ignore_end_gaps=False)


def experiment3():
    """Test bound functionality experiment."""
    # bound dynamic programming, bound value 10
    main_extension('../datasets/extension_2.txt', BLOSUM62(), -15, -2, bound=10)
    # un-bound
    main_extension('../datasets/extension_2.txt', BLOSUM62(), -15, -2, bound=-1)


if __name__ == '__main__':
    experiment1()  # pragma: no cover
    # experiment2() # pragma: no cover
    # experiment3() # pragma: no cover
