# Neohermes

Your machine should have mpi, mpi4py, cmake, python3, zlib1g-dev.

It should also have these python packages: gym, numpy, baselines, pandas, gym_token.

It must have baselines version 0.1.5, which is required to be installed by cloning from https://github.com/openai/baselines and running pip3 install -e .

The baselines version 0.1.5 but install not by cloning from github will not work (the checkpoint_path parameter will not be available).

You may have to cd to this project's root directory before running main.py.

1. screen 
2. ./milk_server
4. Ctrl a + D; screen -L
3. python3 main.py
