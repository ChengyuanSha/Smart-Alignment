from algorithms.RNA import main_RNA
from algorithms.PROT import main_PROT
from algorithms.utils import read_fasta


def main_SPLC(infile):
    dna = max(infile, key=len)
    introns = [s for s in infile if s != dna]
    for i in introns:
        dna = dna.replace(i, "")

    rna = main_RNA(dna)
    pep = main_PROT(rna)

    if pep:
        return pep
    else:
        raise Exception("No exons detected.")


if __name__ == "__main__":
    infile = read_fasta("../datasets/SPLC_1.txt")  # pragma: no cover
    # print(input)
    print(main_SPLC(infile))  # pragma: no cover
