import argparse
import os 
import shutil
from tqdm import tqdm
import logging
from src.utils.common import read_yaml, create_directories
from src.utils.model import log_model_summary
import random
import tensorflow as tf

STAGE = "INITIAL MODEL CREATION"

logging.basicConfig (
    filename = os.path.join("logs", "running_logs.log"),
    level = logging.INFO,
    format = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode = "a"
)


def main(config_path):
    config = read_yaml(config_path)

    params = config["params"]
    logging.info("layers are about to be defined")

    LAYERS = [
    tf.keras.layers.Conv2D(filters = 32, kernel_size = (3,3), input_shape = tuple(params["img_shape"]), activation="relu"),
    tf.keras.layers.MaxPool2D(pool_size=(2, 2), strides=None, padding='valid'),
    tf.keras.layers.Conv2D(filters = 32, kernel_size = (3,3), activation="relu"),
    tf.keras.layers.MaxPool2D(pool_size=(2, 2), strides=None, padding='valid'),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(2, activation = 'softmax')
    ]
    
    logging.info("layers are defined")

    classifier = tf.keras.Sequential(LAYERS)
    logging.info(f"log model summary: \n {log_model_summary(classifier)}")

    classifier.compile(
    loss = params["loss"], 
    optimizer = tf.keras.optimizers.Adam(learning_rate=params["learning_rate"]), 
    metrics = params["metrics"]
    )
    
    path_to_model_dir = os.path.join(config["data"]["local_dir"],
                                config["data"]["model_dir"])

    create_directories(path_to_model_dir)

    path_to_model = os.path.join(path_to_model_dir, 
                                config["data"]["init_model_file"])
    
    classifier.save(path_to_model)

    logging.info(f"model is saved at {path_to_model}")


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