
## Before the session

* You need to have `pytest` (version `6.0.1` ideally) installed.
* You need to be able to run the tests in this repo.


### Installation

To install from conda:


```bash
conda create -y --name tdd-session python==3.7
conda install --force-reinstall -y -q --name tdd-session -c conda-forge --file requirements.txt
conda activate tdd-session
```

Check pytest version:

```bash
pytest --version
```

### Run tests

Run sample test:

```bash
pytest
```

Should return something like:

```bash
============================= test session starts ==============================
...

test/test_sample.py .                                                    [100%]

============================== 1 passed in 0.03s ===============================
```