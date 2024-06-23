# wm01-dragon

## Introduction

This is the course material for WM-01, Summer Semester 2024 (year of the
dragon), Faculty of Biology, University of Freiburg. The instructors are Prof.
Dr. Andrew Straw, Dr. Wolfgang Maier, and Dr. Michael Harrap.

ILIAS link - https://ilias.uni-freiburg.de/goto.php?target=crs_3529938&client_id=unifreiburg

## Run interactively at https://strawlab-rp2.zoologie.uni-freiburg.de

You have the choice of running the exercises in the class either (A) on our
Jupyter server at https://strawlab-rp2.zoologie.uni-freiburg.de (login details
will be discussed in class) or (B) on your own PC.

To run on your PC, we recommend using
[Anaconda](https://www.anaconda.com/download) to install Python and the
dependencies we will use. We will help you install Anaconda and the packages we
use in the course. Until Anaconda is installed on your own PC, for the first few
days (or for the entire course), you may use our Jupyter server. This will be
taken offline shortly after the course is done.

## Installation with Anaconda

Download the Anaconda Distribution from [here](https://www.anaconda.com/download).

### Creating your own Anaconda environment

The package versions used for the class are specified in the `environment.yml`
file. The package versions here are equal to package versions installed with
`Anaconda3-2024.02-1-MacOSX-arm64.pkg` downloaded and installed on 2024-06-23. Therefore, you likely do not need to install this way. However, if you already have anaconda installed and want to create a new Anaconda environment specifically for this class, run the following commands in the Anaconda terminal:

```
conda env create -f environment.yml
conda activate wm01-dragon
```

## The Python Tutor - extremely highly recommended

http://pythontutor.com/

## Troubleshooting

### Note for macOS users

Before starting `jupyter notebook` from the command line, you may like to type:

    ulimit -n 4096

This will solve [OSError: [Errno 24] Too many open files](https://github.com/jupyterlab/jupyterlab/issues/6727).

## Code of conduct

Anyone who interacts with this software in any space, including but not limited
to this GitHub repository, must follow our [code of
conduct](code_of_conduct.md).
