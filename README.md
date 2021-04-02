[![Codacy Badge](https://api.codacy.com/project/badge/Grade/c6150e482d28425a8895843df1b2a640)](https://app.codacy.com/gh/ChengyuanSha/Smart-Alignment?utm_source=github.com&utm_medium=referral&utm_content=ChengyuanSha/Smart-Alignment&utm_campaign=Badge_Grade_Settings)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/bff56bab2b5741ccade6610ce3e0df49)](https://www.codacy.com/gh/ChengyuanSha/Smart-Alignment/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ChengyuanSha/Smart-Alignment&amp;utm_campaign=Badge_Coverage)

## Global Alignment with Scoring Matrix and Affine Gap Penalty (In development)

## Development Notes

* Every Rosalind node should have its own file in the format ```ACRN.py``` (Put inside algorithms folder) 
  where ```ACRN``` is the acronym for the node in the tree view
  
* Name the main function in each node main_XXX, eg. main function in ```ACRN.py``` should be ```main_ACRN(...)```

* Ideally, main_ACRN(...) should only has **fname** (filename) as input (looks like it is in most cases)

* Name testing function test_function_name, eg. for ```ACRN.py``` -> ```test_ACRN.py```

* Use following way to read input files. eg.
```python
import os
script_dir = os.path.dirname(__file__) # absolute dir the script is in
rel_path = "../datasets/DNA_1.txt"
abs_file_path = os.path.join(script_dir, rel_path)
```

* multiple tests per function, first two positive, last one negative

* unit test doc: https://docs.python.org/3/library/unittest.html

* use of doc string: https://www.python.org/dev/peps/pep-0257/

* Check coverage: https://coverage.readthedocs.io/en/coverage-5.5/

```python
coverage run -m unittest discover
```
