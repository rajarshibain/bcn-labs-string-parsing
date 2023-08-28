import os
# Contains absolute paths of all the important folders in code

PROJECT_DIR = (str(os.path.realpath(__file__)))[:-19]

# Global random state value

RANDOM_STATE = 42 #int(os.environ.get("RANDOM_STATE",'42'))

# Data folder

DATA_DIR= os.path.join(PROJECT_DIR, "data")

RAW_DATA_DIR= os.path.join(DATA_DIR, "raw")

OUTPUT_DATA_DIR = os.path.join(DATA_DIR, "outputs")

# src folder

SRC_DIR= os.path.join(PROJECT_DIR, "src")


# config folder

CONFIG_DIR= os.path.join(PROJECT_DIR, "config")

