# Development Guide


## Create a conda environment.
Check  [Install Conda Guide](https://conda.io/docs/user-guide/install)  for Python3.6 .


````bash
conda create python=3.6.0 -n venv
````

For activate environment

````bash
conda activate venv
````

You will see in your prompt

````bash
(venv) ~/Projects/open-charade/chargeback
````

Install requirements for development environment
````bash
pip install -r requirements-dev.txt
````
To deactivate

````bash
conda deactivate
````

## Make a release

You need to tag the commit to deploy a new release in pypy.