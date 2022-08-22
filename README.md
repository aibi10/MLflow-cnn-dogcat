# mlflow-project-template

template for mlflow

# create environment (bash)

```bash
conda create --prefix ./env python=3.7 -y
```

# conda activate environment(bash)

```bash
conda activate ./env
```

# install the requirements

```bash
pip install -r requirements.txt
```

# create conda.yaml(bash)

```bash
conda env export > conda.yaml
```

# command to run MLproject file

```bash
mlflow run . --no-conda
```

# run any specific entry point

```bash
mlflow run . -e get_data --no-conda
```

# to run with a different configuration

```bash
mlflow run . -e get_data -P config=configs/name_of_config_file.yaml --no-conda
```
