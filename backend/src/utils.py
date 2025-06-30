import json
import logging

utils_logger = logging.getLogger(__name__)


def create_json_file(json_file_path):
    try:
        utils_logger.debug(f"Creating json file '{json_file_path}'.")
        with open(json_file_path, 'w') as write_json_file:
            json.dump({}, write_json_file)
    except PermissionError as e:
        utils_logger.error(f"Permission missing to create file in path'{json_file_path}': {e}")
        raise e
    except IOError as e:
        raise e


def read_contents_from_json_file(json_file):
    try:
        utils_logger.debug(f"Reading json_file {json_file}")
        with open(json_file, 'r') as read_json_file:
            return json.load(read_json_file)
    except FileNotFoundError:
        utils_logger.error(f"JSON file '{json_file}' does not exist.")
        utils_logger.debug(f"Creating file '{json_file}'")
        create_json_file(json_file)
        return read_contents_from_json_file(json_file)
    except json.JSONDecodeError as e:
        utils_logger.error(f"Error while reading json file '{json_file}'. JSON file contains invalid formatting: {e}")
        raise e
