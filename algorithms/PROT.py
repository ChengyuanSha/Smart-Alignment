def codons():
    '''
    Helper function which creates a mapping of 3-tuples representing RNA codons
    mapped onto their corresponding amino acids. Asterisk (*) represents a
    STOP codon.
    '''
    bases = ["U", "C", "A", "G"]
    
    aa = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
    codons = [x + y + z for x in bases for y in bases for z in bases]
    return dict(zip(codons, aa))
    
def read_input(fname):
    """Read txt file containing A DNA string."""
    with open(fname, 'r') as f:
        return f.read()

def main_PROT(rna):
    mapping = codons()
    pep = ""
    
    for frame in range(0, len(rna), 3):
        codon = rna[frame:frame+3]
        aa = mapping.get(codon, "*")
        if aa != "*":
            pep += aa
        else:
            break

    return pep

if __name__ == "__main__":
    rna = read_input("../datasets/PROT_3.txt")
    print(main_PROT(rna))