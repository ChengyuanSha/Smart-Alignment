def read_input(fname):
    """Read txt file containing A DNA string."""
    with open(fname, 'r') as f:
        return f.read()

def main_SUBS(input):
    
    seq, motif = input.strip().split("\n")
    
    indices = []
    for n in range(len(seq)):
        if seq.startswith(motif, n):
            indices.append(n+1)
            
    return indices
    
if __name__ == "__main__":
    input = read_input("../datasets/SUBS_1.txt")
    print(main_SUBS(input))