# prose

prose is a python package to reduce and analyse data from telescope observations. Its primary goal is the production of differential light curves from raw uncalibrated FITS images.

<p align="center">
  <img width="400" src="docs/source/prose.png">
</p>

## Installation

```shell
pip install git+https://github.com/LionelGarcia/prose
```

prose runs more safely in its own [virtual environment](https://docs.python.org/3/tutorial/venv.html) and is tested on Python 3.6.

### example on OSX

create your [virtualenv](https://docs.python.org/3/tutorial/venv.html) and activate it

```shell
python3.6 -m venv prose_env
source prose_env/bin/activate.bin
```

and

```shell
python3.6 -m pip install git+https://github.com/LionelGarcia/prose
```

Applicable to Linux-based and Windows OS