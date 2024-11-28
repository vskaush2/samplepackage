# samplepackage

This is a sample package designed to be used as a template for creating a Python package.

## Installation

If `samplepackage` is published in PyPI, then run
```bash
$ pip install samplepackage
```

Otherwise, download the package from GitHub, change directory to the location of `samplepackage`, and run
```bash
$ pip install .
```
It is highly recommended to use a virtual environment when installing `samplepackage`. 
Please see the [Virtual Environments](#Virtual-Environments) section for more information on creating a virtual environment.

## Usage

`samplepackage` can be used as follows:

```python
from samplepackage.script import *
SC=SampleClass(np.array([1,2]),np.array([3,4]))
SC.sample_method(2.0,3.0) # Outputs array([11., 16.])
```

## Contributing

Interested in contributing? Check out the contributing guidelines. 
Please note that this project is released with a Code of Conduct. 
By contributing to this project, you agree to abide by its terms.

## License

`samplepackage` was greatly inspired by the `pycounts` package that was created by Tomas Beuzen. It is licensed under the terms
of the MIT license.

