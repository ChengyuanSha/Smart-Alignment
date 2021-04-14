from algorithms.PROT import main_PROT, codons
    
def read_input(fname):
    '''
    Read txt file containing A DNA string.
    '''
    with open(fname, 'r') as f:
        return f.read()

def read_fasta(fname):
    ''' 
    Read in a Fasta file and returns a list of sequences.
    '''
    temp = []
    seqs = []
    
    with open(fname, 'r') as f:
        for line in f.readlines():
            if line.startswith('>'):
                temp.append(line[1:].strip())
                seqs.append('')
            else:
                seqs[-1] += line.strip()
                 
    return seqs
    
def main_SPLC(input):
    rna = max(input, key = len)
    intron = [s for s in input if s != rna]
    
    for i in introns:
        rna = rna.replace(i, "")
        
    pep = main_PROT(rna)
    
    if pep:
        return pep
    else:
        raise Exception("No exons detected.")
    
if __name__ == "__main__"
    input = read_fasta("../datasets/SPLC_1.txt")
    print(main_SPLC(input))
    