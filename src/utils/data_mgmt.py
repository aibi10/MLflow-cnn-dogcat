import os
from PIL import Image 
import imghdr
import logging
from src.utils.common import create_directories



def validate_image(config: dict) -> None:
    PARENT_DIR = config['data']['PARENT_DIR']
    BAD_DATA_DIR = config['data']['BAD_DATA_DIR']
    logging.info("function execution started")
    create_directories(BAD_DATA_DIR)
    for dirs in os.listdir(PARENT_DIR): 
        full_path = os.path.join(PARENT_DIR, dirs)
        for images in os.listdir(full_path):
            path_to_images = os.path.join(full_path, images)
            try:
                img = Image.open(path_to_images)
                img.verify()
                #print(f"{path_to_images} is verified")

                if len(img.getbands()) != 3 or imghdr.what(path_to_images) not in ['jpeg', 'png', 'jpg']:
                    logging.info(f"{path_to_images} is bad image, it is being moved to {BAD_DATA_DIR}")
                    shutil.move(path_to_images, BAD_DATA_DIR)
            except Exception as e:
                logging.info(f"{path_to_images} is bad image, it is being moved to {BAD_DATA_DIR}")
                logging.exception(e)
                shutil.move(path_to_images, BAD_DATA_DIR)