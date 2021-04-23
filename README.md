[![Codacy Badge](https://api.codacy.com/project/badge/Grade/c6150e482d28425a8895843df1b2a640)](https://app.codacy.com/gh/ChengyuanSha/Smart-Alignment?utm_source=github.com&utm_medium=referral&utm_content=ChengyuanSha/Smart-Alignment&utm_campaign=Badge_Grade_Settings)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/bff56bab2b5741ccade6610ce3e0df49)](https://www.codacy.com/gh/ChengyuanSha/Smart-Alignment/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ChengyuanSha/Smart-Alignment&amp;utm_campaign=Badge_Coverage)

## Global Alignment with Scoring Matrix, Custom Weight, Affine Gap Penalty and Bounded Dynamic Programming (DP) Acceleration.

## Introduction

* Every Rosalind node have its own file in the format ```ACRN.py``` (in algorithms folder) 
  where ```ACRN``` is the acronym for the node in the tree view
  
* The main function in each node is main_XXX, eg. main function in ```ACRN.py``` is```main_ACRN(...)```
 the main function input is what it says on the rosalind site.

* Testing function is named test_function_name, eg. for ```ACRN.py``` -> ```test_ACRN.py```

* There are multiple tests per function, first two are positive, last one is negative. 
  Test data are named form 1-3 in dataset (except for extension, there are 6 dataset, first 3 are used by experiment).

## Code quality

Code quality and test coverage is ensured by the continuous integration server [Codacy](https://www.codacy.com/)
and python [Coverage](https://coverage.readthedocs.io/en/coverage-5.5/).
Codacy uses Radon by default to calculate metrics from the source code.

We achieved 100% coverage on all algorithm files. Check Coverage:
```python
coverage run -m unittest discover
coverage report
```

## Running Instruction

Please install all requirements from `requirements.txt`.

`figures.py `contains the `efficiency experiment` (Comparing time efficiency between unbounded algorithm 
and bounded acceleration) and
`comparing optimal scores experiment` (Comparing alignment scores from bounded algorithm with the 
optimal scores from unbounded algorithm).

`experiments.py` contains all other experiments performed by us.

## Function usage:

```text
GAFF_extended(s, t, scoring_matrix, gap, gap_ext, conserved_seq="", conserved_strength=0, bound=-1,
                  ignore_start_gaps=False, ignore_end_gaps=False, auto_bound = False):

    Global Alignment with Scoring Matrix, Custom Weight, Affine Gap Penalty and Bounded DP Acceleration.

    Inputs: Two protein strings s and t in FASTA format.
            conserved_seq: will increase the weight on the sequence.
            conserved_strength: weight on conserved_seq.
            bound: Define the range of bound dynamic programming. Negative number will run unbound version.
            auto_bound: Auto calculate the bound size using DNA length difference.
            ignore_start_gaps: ignoring start gaps in alignment, default False.
            ignore_end_gaps: ignoring end gaps in alignment, default False.

    Returns: The maximum alignment score between s and t, followed by two augmented strings
             s′ and t′ representing an optimal alignment of s and t.
```







