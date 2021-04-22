import random
from GAFF_extension import main_extension
from algorithms.utils import BLOSUM62
import time
import numpy as np

def generate_DNA_data(length):
    """Generate random DNA of variable length."""
    return ''.join(random.choice('ATCG') for _ in range(length))


def write_2dna_to_file(length, sec_len_divisor=1.0):
    """Write 2 DNA to file in fasta format."""
    with open('../datasets/extension_3.txt', 'w') as f:
        f.write(">Test seq1\n")
        f.write(generate_DNA_data(length))
        f.write("\n>Test seq2\n")
        f.write(generate_DNA_data(int(length / sec_len_divisor)))


def compare_efficiency():
    """Compare unmodified VS improved version."""
    time_ori, time_bound, x_range = [], [], []
    for dna_len in range(10, 601, 10): # 10, 601, 10
        write_2dna_to_file(dna_len)
        print("Unbounded Version: ")
        temp1 = []
        for _ in range(10):
            start = time.time()
            main_extension('../datasets/extension_3.txt', BLOSUM62(), -15, -2, bound=-1,
                           ignore_start_gaps=False, ignore_end_gaps=False)
            temp1.append(time.time() - start)
        print("Time used:", )
        time_ori.append(round(sum(temp1) / len(temp1), 6))
        print("Bounded dynamic programming: ")
        temp2 = []
        for _ in range(10):
            start = time.time()
            main_extension('../datasets/extension_3.txt', BLOSUM62(), -15, -2, bound=10,
                           ignore_start_gaps=False, ignore_end_gaps=False)
            temp2.append(time.time() - start)
        time_bound.append(round(sum(temp2) / len(temp2), 6))
        x_range.append(dna_len)
    # produce data for graph
    print(*list(zip(x_range, time_ori)), sep='')
    print(*list(zip(x_range, time_bound)), sep='')


def comparing_optimal_scores(repeat, dna_len):
    """Compare unbound VS bound version in terms of optimal scores."""
    x_range, percentage = [], []
    for divisor in np.linspace(1,3,21): # 1,3,21
        scores_ori, scores_bound = [], []
        for _ in range(repeat):
            write_2dna_to_file(dna_len, sec_len_divisor=divisor)
            max_score, _, _ = main_extension('../datasets/extension_3.txt', BLOSUM62(), -15, -2, bound=-1,
                                             ignore_start_gaps=False, ignore_end_gaps=False)
            scores_ori.append(max_score)
            max_score, _, _ = main_extension('../datasets/extension_3.txt', BLOSUM62(), -15, -2, bound=10,
                                             ignore_start_gaps=False, ignore_end_gaps=False)
            scores_bound.append(max_score)
        x_range.append(divisor)
        common_scores = len([i for i, j in zip(scores_ori, scores_bound) if i == j])
        percentage.append(round(common_scores/repeat*100, 4)) # %
    # produce data for graph
    print(*list(zip(x_range, percentage)), sep='')



if __name__ == '__main__':
    # print(generate_DNA_data(100)) # pragma: no cover
    # write_2dna_to_file(1000) # pragma: no cover
    # compare_efficiency()  # pragma: no cover
    comparing_optimal_scores(50, 30)
