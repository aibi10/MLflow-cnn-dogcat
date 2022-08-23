import argparse
import os 
import shutil
from tqdm import tqdm
import logging
from src.utils.common import read_yaml, create_directories
import random
import tensorflow as tf
import mlflow

STAGE = "Training"

logging.basicConfig (
    filename = os.path.join("logs", "running_logs.log"),
    level = logging.INFO,
    format = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode = "a"
)


def main(config_path):
    config = read_yaml(config_path)

    params = config["params"]
    ## some preprocessing
    PARENT_DIR = config['data']['PARENT_DIR']
    logging.info(f"reading dataset from {PARENT_DIR}")

    train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    PARENT_DIR,
    validation_split=params["validation_split"],
    subset = "training",
    seed = params["seed"],
    image_size=params["img_shape"][:-1],
    batch_size=params["batch_size"],
    
    )

    val_ds = tf.keras.preprocessing.image_dataset_from_directory(
        PARENT_DIR,
        validation_split=params["validation_split"],
        subset = "validation",
        seed = params["seed"],
        image_size=params["img_shape"][:-1],
        batch_size=params["batch_size"],
        
    )

    logging.info(f"reading of dataset is done from {PARENT_DIR}")

    train_ds = train_ds.prefetch(buffer_size = params["buffer_size"])
    val_ds = val_ds.prefetch(buffer_size = params["buffer_size"])

    ## load the model
    path_to_model_dir = os.path.join(config["data"]["local_dir"],
                                config["data"]["model_dir"]) 

    path_to_model = os.path.join(path_to_model_dir, 
                                config["data"]["init_model_file"])
    try:
        logging.info(f"loading of model from {path_to_model}")
        classifier = tf.keras.models.load_model(path_to_model)
        logging.info(f"loading of model is donefrom {path_to_model}")
    except Exception as e:
        logging.info("some error occured while loading the file")
        logging.exception(e)

    ## train
    try:
        logging.info("training started .............")
        classifier.fit(train_ds, epochs=params['epochs'], validation_data=val_ds)
        logging.info("training is done ..............")
    except Exception as e:
        logging.info("some error occured during training")
        logging.exception(e)

    train_model_file = os.path.join(path_to_model_dir, 
                                config["data"]["trained_model_file"])
    try:
        logging.info(f"saving model at {train_model_file}")
        classifier.save(train_model_file)
        logging.info(f"model has been saved at {train_model_file}")

    except Exception as e:
        logging.info("error occured during saving of model")
        logging.exception(e)
    
    with mlflow.start_run() as run:
        mlflow.log_params(params)
        mlflow.keras.log_model(classifier, "model")

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default = "configs/config.yaml")
    parsed_args = args.parse_args()

    try:
        logging.info("\n***************************")
        logging.info(f">>>>>>>>>>> stage   {STAGE}   started <<<<<<<<<<")
        main(config_path = parsed_args.config)
        logging.info(f">>>>>>>>> stage  {STAGE}   completed <<<<<<<<<<<")
    except Exception as e:
        logging.exception(e)
        raise e 