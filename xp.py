# %% Imports
from pathlib import Path

import numpy as np

# %% Change the parameters' values of the xp
a = 2
b = -1
c = 10  


# %% Do not change BELOW ###
def f(x, y, z):
    inp = np.arange(-20, 20, 0.2)
    return x * (inp ** 2) + y * inp + z


# %% Script entry point
if __name__ == '__main__':
    # %% Script entry point
    ## Compute out
    out = f(a, b, c)

    ## Dump out.npy
    np.save('out', out)

    ## Compute Score
    assert Path('target.npy').exists(), \
        'Have you followed the installation instruction ? (Try running "dvc pull && dvc checkout")'

    square_err = np.mean((np.load('target.npy') - out) ** 2)

    ## Write square_err.metric
    Path('square_err.metric').write_text(f"{square_err}\n")
