import algorithms.utils as utils


def main_LCSM(fname):
    dataset = utils.read_fasta(fname)
    substr = ''
    if len(dataset) > 1 and len(dataset[0]) > 0:
        for i in range(len(dataset[0])):
            for j in range(len(dataset[0]) - i + 1):
                if j > len(substr) and all(dataset[0][i:i + j] in x for x in dataset):
                    substr = dataset[0][i:i + j]
    return substr


if __name__ == '__main__':
    print(main_LCSM('../datasets/LCSM_1.txt'))  # pragma: no cover

