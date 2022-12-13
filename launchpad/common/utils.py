import os
from argparse import Namespace

import yaml
import argparse
import logging


def read_config(config_file) -> dict:
    # Check if the config file exists
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"Config file {config_file} not found")

    with open(config_file, "r") as f:
        try:
            config = yaml.safe_load(f)
        except yaml.YAMLError as e:
            raise e

    return config


def init_args() -> Namespace:
    # Set up the argument parser
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-loglevel",
        metavar="--loglevel",
        type=int,
        default=3,
        help="Loglevel [0,5]")

    return parser.parse_args()


def init_logging(args) -> None:
    # Set up logging
    filename = "%slog" % __file__[:-2]
    log_format = "{asctime} {levelname:<8} {message}"
    logging.basicConfig(
        level=args.loglevel * 10,
        format=log_format,
        style="{",
        handlers=[
            logging.FileHandler(filename),
            logging.StreamHandler()
        ]
    )
