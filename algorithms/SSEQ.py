from algorithms.SPLC import read_fasta

def subseq_search(seq, target):
    '''
    
    '''
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
    
    
if __name__ == "__main__"
    input = read_fasta("../datasets/SSEQ_1.txt")
    print(main_SSEQ(input))