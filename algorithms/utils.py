"""
utils file:
Common functions used by questions
"""


def read_fasta(fname):
    header = ''
    for line in fname:
        if line.startswith('>'):
            if header:
                yield header, dna
            header, dna = line[1:].rstrip().split()[0], ''
        elif header:
            dna += line.rstrip()
    if header:
        yield header, dna


def get_dna(fname):
    with open(fname) as f:
        fasta_as_list = []
        for i in f:
            fasta_as_list.append(i)
    just_dna = []
    for line in read_fasta(fasta_as_list):
        just_dna.append(line[1])
    return just_dna
