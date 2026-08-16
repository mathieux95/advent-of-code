## advent-of-code

Python solutions for [Advent of Code 2018](https://adventofcode.com/2018).


### Setup
Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```

Install the project and its dependencies:
```bash
pip install -e .
```


Run all tests from project root:
```bash
pytest 
```

for for more detailed test output, use:
```bash
pytest -v
```

To run tests for a specific day:
```bash
pytest aoc2018/tests/test_day_01.py
```


### Solutions
Run a specific Advent of Code day from the project root:
```bash
python -m aoc2018.main 1
```

or, multiple days can be executed at once:
```bash
python -m aoc2018.main 1 2
```

Each day expects its input file in `aoc2018/inputs/` using the name `input_day_XX.txt`.