import json
import yaml

class ConfigParser:
    @staticmethod
    def parse_json(file_path):

        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: File not found at {file_path}")
            return {}
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON at {file_path}: {e}")
            return {}

    @staticmethod
    def parse_yaml(file_path):

        try:
            with open(file_path, 'r') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            print(f"Error: File not found at {file_path}")
            return {}
        except yaml.YAMLError as e:
            print(f"Error: Invalid YAML at {file_path}: {e}")
            return {}

    @staticmethod
    def parse_ini(file_path):
        """
        Parse an INI configuration file.

        Args:
            file_path (str): The path to the INI file.

        Returns:
            dict: The parsed configuration data.
        """
        import configparser
        config = configparser.ConfigParser()
        try:
            config.read(file_path)
            return {section: dict(config.items(section)) for section in config.sections()}
        except configparser.Error as e:
            print(f"Error: Invalid INI at {file_path}: {e}")
            return {}

# Example usage:
config_parser = ConfigParser

# Parse a JSON file
json_file_path = 'config.json'
json_config = config_parser.parse_json(json_file_path)
print(f"JSON Config: {json_config}")

# Parse a YAML file
yaml_file_path = 'config.yaml'
yaml_config = config_parser.parse_yaml(yaml_file_path)
print(f"YAML Config: {yaml_config}")

# Parse an INI file
ini_file_path = 'config.ini'
ini_config = config_parser.parse_ini(ini_file_path)
print(f"INI Config: {ini_config}")