#class car:
 #  def __init__(self,name,age):
      #  self.name=name
       # self.age=age
    #@classmethod
    #def m1(cls):
    #    print("my name is age is ")
#c1=car("sanku","20")
#print(c1.model)
#print(c1.m1())
import json
import yaml
import os

class ConfigParser:
    # Class variables for default configuration file paths and formats
    DEFAULT_CONFIG_FILE_PATH = '/etc/config.json'
    DEFAULT_CONFIG_FORMAT = 'json'

    @staticmethod
    def parse_json(file_path=None):
        if file_path is None:
            file_path = ConfigParser.DEFAULT_CONFIG_FILE_PATH
        with open(file_path, 'r') as f:
            return json.load(f)

    @staticmethod
    def parse_yaml(file_path=None):
        if file_path is None:
            file_path = ConfigParser.DEFAULT_CONFIG_FILE_PATH
        with open(file_path, 'r') as f:
            return yaml.safe_load(f)

    @staticmethod
    def parse_config(file_path=None, format=None):
        if file_path is None:
            file_path = ConfigParser.DEFAULT_CONFIG_FILE_PATH
        if format is None:
            format = ConfigParser.DEFAULT_CONFIG_FORMAT
        if format == 'json':
            return ConfigParser.parse_json(file_path)
        elif format == 'yaml':
            return ConfigParser.parse_yaml(file_path)
        else:
            raise ValueError(f"Unsupported format: {format}")

    @staticmethod
    def get_default_config():
        return ConfigParser.parse_config()

# Example usage:
config = ConfigParser.get_default_config()
print(config)

config_yaml = ConfigParser.parse_yaml('/path/to/config.yaml')
print(config_yaml)

config_json = ConfigParser.parse_json('/path/to/config.json')
print(config_json)