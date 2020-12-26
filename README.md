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

Run sample test:

```bash
pytest
```

Should return something like:

```bash
============================= test session starts ==============================
platform darwin -- Python 3.7.6, pytest-6.0.1, py-1.9.0, pluggy-0.13.1
rootdir: /Users/davidmasip/Documents/Others/tdd-session
plugins: mock-3.3.1, hypothesis-5.5.4, arraydiff-0.3, remotedata-0.3.2, openfiles-0.4.0, doctestplus-0.5.0, astropy-header-0.1.2
collected 1 item

test/test_sample.py .                                                    [100%]

============================== 1 passed in 0.03s ===============================
```