# mlflow-project-template

template for mlflow

# create environment (bash)

conda create --prefix ./env python=3.7 -y

# conda activate environment(bash)

conda activate ./env

# install the requirements

pip install -r requirements.txt

# create conda.yaml(bash)

conda env export > conda.yaml

# command to run MLproject file

mlflow run . --no-conda

# run any specific entry point

mlflow run . -e get_data --no-conda

# to run with a different configuration

mlflow run . -e get_data -P config=configs/name_of_config_file.yaml --no-conda
