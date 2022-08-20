conda create --prefix ./env python=3.7 -y
source activate ./env
pip install -r "C:\Users\ASUS\Downloads\mlflow-cnn-dogcat\MLflow-cnn-dogcat\requriements.txt"
conda env export > conda.yaml