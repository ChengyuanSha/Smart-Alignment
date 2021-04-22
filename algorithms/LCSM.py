import algorithms.utils as utils


def main_LCSM(fname):
    """

    Finds the longest common substring of 100 or less strings from a FASTA format file
    :param fname:txt file in FASTA format
    :return:Longest common substring
    """
    try:
        dataset = utils.read_fasta(fname)
    except IndexError:
        raise IndexError("File not in FASTA format")
    substr = ''
    if len(dataset) > 1 and len(dataset[0]) > 0:
        for i in range(len(dataset[0])):
            for j in range(len(dataset[0]) - i + 1):
                if j > len(substr) and all(dataset[0][i:i + j] in x for x in dataset):
                    substr = dataset[0][i:i + j]
    else:
        raise ValueError("Invalid input: Input must be more than 1 string, and strings must be non-zero")
    return substr


if __name__ == '__main__':
    print(main_LCSM('../datasets/LCSM_5.txt'))  # pragma: no cover

