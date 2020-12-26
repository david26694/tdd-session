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

