
# Project Title

This is a package that takes in X and y as training data and predicts two outputs as y1 and y2 for any given test data.
This package removes the limitation of just have one target feature in machine learning.


## Contributing

Contributions are always welcome!

The package needs to be extend to predict non-categorical variables.

Please adhere to this project's `code of conduct`.

  
## Installation 

To install this package run

```bash
  pip install multilabel
```

  
## Feedback

If you have any feedback, please reach out to me at owodunniabraham@gmail.com
  
## License

[MIT](https://choosealicense.com/licenses/mit/)

  
## Usage/Examples

[Notebook](https://github.com/owos/Multilabel/blob/main/use_case_of_mutlilabel.ipynb)
```bash
  from multilabel import BilableClassifier
  model = BilableClassifier(xgboost())
```
  