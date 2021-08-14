from yaml import load
import yaml

# load configuration file to dictionary
with open("../config.yaml", "r") as configFile:
    config = yaml.load(configFile, Loader=yaml.SafeLoader)

