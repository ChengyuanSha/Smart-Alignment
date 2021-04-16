"""
utils file:
Common functions used by questions
"""
import pandas as pd


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


def read_score_matrix(fname):
    '''
    Read a text file of a scoring matrix.
    Return a score matrix dataframe with row and column as amino acids.
    '''
    return pd.read_csv(fname, delimiter=r"\s+", header=0, index_col=0)


def BLOSUM62():
    '''Return a BLOSUM62 score matrix dataframe.'''
    return read_score_matrix('../datasets/BLOSUM62.txt')
