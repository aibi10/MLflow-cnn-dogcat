import argparse
import os 
import shutil
from tqdm import tqdm
import logging
from src.utils.common import read_yaml, create_directories
from src.utils.data_mgmt import validate_image
import random

STAGE = "DATA LOAD"

logging.basicConfig (
    filename = os.path.join("logs", "running_logs.log"),
    level = logging.INFO,
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode = "a"
)


def main(config_path):
    config = read_yaml(config_path)
    local_dir = config['data']['local_dir']
    create_directories(local_dir)                       # a folder is created with the name 'data'
    data_file = config['data']['file_name']
    data_file_path = os.path.join(local_dir, data_file)

    validate_image(config)

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