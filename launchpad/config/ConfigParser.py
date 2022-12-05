import yaml
import os


class ConfigParser:
    def __init__(self, config_file: str = "config.yml"):
        self.config_file = config_file
        self.config = None

    def load_config(self):
        # Check if the config file exists
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"Config file {self.config_file} not found")

        with open(self.config_file, "r") as f:
            try:
                self.config = yaml.safe_load(f)
            except yaml.YAMLError as e:
                raise e

    def get_pads_config(self) -> dict:
        return self.config.get("pads")

    def get_potentiometers_config(self) -> dict:
        return self.config.get("potentiometers")

    def get_play_rec_config(self) -> dict:
        return self.config.get("play_rec")
