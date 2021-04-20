from algorithms.SPLC import read_fasta

def main_SSEQ(strings):
    '''
    This function takes 2 strings as input and finds indices
    corresponding to one possible subsequence position of the
    target string in the sequence.
    '''
    seq, target = strings
    targets = list(target)
    indices = []
    i = 0
    for loc, s in enumerate(seq):
        if s == targets[i]:
            indices.append(str(loc + 1))
            if i < len(targets) - 1:
                i += 1
            else:
                break
    return indices
    
if __name__ == "__main__":
    strings = read_fasta("../datasets/SSEQ_2.txt")
    print(main_SSEQ(strings))