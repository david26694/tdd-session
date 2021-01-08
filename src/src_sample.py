

def ceil(x):
    if x < 0:
        if x != int(x):
            return int(x) - 1
    return int(x)