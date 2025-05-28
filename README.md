# Sum-Pairs

Thanks to this package you can find pairs of numbers that sum to the same value.


## Usage

You can use the `find_pairs` function from the `sum_pairs` module to find pairs of numbers that sum to the same value.

```python
from sum_pairs import find_pairs

pairs = find_pairs([1, 2, 3, 4, 5])
```
Should output:
```
Pairs: (1, 4), (2, 3) have sum 5
Pairs: (1, 5), (2, 4) have sum 6
Pairs: (2, 5), (3, 4) have sum 7
```


## Local development

This package uses [uv](https://docs.astral.sh/uv/) package manager. You need to
install it first. Follow the instructions in the [uv documentation](https://docs.astral.sh/uv/getting-started/installation/) to set it up.

Install dependencies:
```shell
uv sync
```
`uv` will create a virtual environment (`./.venv`) and install all the required dependencies.
Activate the virtual environment:
```shell
source .venv/bin/activate
```

Install pre-commit hooks:
```shell
pre-commit install
```

Run tests
```
pytest
```

## Build & installation
To build the package, run:
```shell
uv build
```
To install the package from the built files, run:
```shell
pip install dist/sum_pairs-0.1.0-py3-none-any.whl
# Or from tar.gz
pip install dist/sum_pairs-0.1.0.tar.gz
```

You can also install the package directly from github:
```shell
pip install "git+ssh://git@github.com/umatbro/sum-pairs.git"
```
