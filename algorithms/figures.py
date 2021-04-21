import random
from GAFF_extension import main_extension
from algorithms.utils import BLOSUM62
import time


def generate_DNA_data(length):
    """Generate random DNA of variable length."""
    return ''.join(random.choice('ATCG') for _ in range(length))


def write_2dna_to_file(length):
    """Write to file in fasta format."""
    with open('../datasets/extension_3.txt', 'w') as f:
        f.write(">Test seq1\n")
        f.write(generate_DNA_data(length))
        f.write("\n>Test seq2\n")
        f.write(generate_DNA_data(length))


def compare_efficiency():
    """Compare unmodified VS improved version."""
    time_ori, time_bound, x_range = [], [], []
    for dna_len in range(10, 601, 10):
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
    print(*list(zip(x_range, time_ori)), sep='')
    print(*list(zip(x_range, time_bound)), sep='')


if __name__ == '__main__':
    # print(generate_DNA_data(100)) # pragma: no cover
    # write_2dna_to_file(1000) # pragma: no cover
    compare_efficiency()  # pragma: no cover
