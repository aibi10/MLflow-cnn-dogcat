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

 # create conda.yaml
 conda env export > conda.yaml