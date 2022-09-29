# Conda Environment Setup

We are going to use the Ana(conda) package manager to setup our Python Pybliometrics development
environment. 

See the Conda documentation for managing environments:
https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html


Here is the recipe we will use within a terminal (or Anaconda Prompt on Windows):


```console
conda create --name my-scopus-env
conda activate my-scopus-env
conda install -c conda-forge jupyterlab pandas matplotlib pip
pip install pybliometrics

```

To launch a jupyter notebook, type `jupyter lab`
