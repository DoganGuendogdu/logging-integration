import json
import logging
from itertools import count

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


def write_contents_to_json_file(json_file_path, contents: dict):
    try:
        utils_logger.debug(f"Writings contents to JSON file '{json_file_path}': {contents}")
        with open(json_file_path, 'w') as write_json_file:
            json.dump(contents, write_json_file, indent=4)
    except PermissionError as e:
        utils_logger.error(f"Permission missing to create file in path'{json_file_path}': {e}")
        raise e


# Goal is to replace existing data in json file by providing a dict of data
# json_data: contents from a JSON file as dict
# new_data: data which will be written into JSON file
# key_name: name of key to extract the corresponding value
def replace_values_json_file(json_data: dict, new_data: dict, key_name: str):
    # check if specified key exists in JSON file
    utils_logger.debug(f"Checking if key '{key_name}' exists in JSON file with content: {json_data}")
    # create structure if it does not exist already using directly new data
    if key_name not in json_data.keys():
        utils_logger.error(f"Key '{key_name}' does not exist in json data: '{json_data}'.")
        utils_logger.debug(f"Creating structure using new data: '{new_data}'")
        json_data[key_name] = [new_data]
        return json_data

    # if structure already exists, replace old data with new data
    # get value of json object by specifying key. Return value is a list of dictionary objects.
    json_data_with_key_specified = json_data.get(key_name)
    utils_logger.debug(f"Extracting value for key '{key_name}': {json_data_with_key_specified}")

    # iterate over the list of dictionaries to check if new_data structure already exists.
    # for that, check if a given dictionary has all keys of new_data
    new_data_keys = new_data.keys()
    utils_logger.debug(f"Extracting keys from new data: {new_data_keys}")
    for i in count(start=0, step=1):
        try:
            utils_logger.debug(f"Check if keys '{new_data_keys}' exist in JSON object value.")
            # if the relevant dict object is found, replace it with the new values
            if new_data_keys == json_data_with_key_specified[i].keys():
                utils_logger.debug(f"Structure with keys exist in JSON file: '{new_data_keys}'.")
                json_data.get(key_name)[i].update(new_data)
                return json_data
            # if the relevant dict does not exist, append it to list of dict objects
        except IndexError as e:
            utils_logger.debug(f"Keys '{new_data_keys}' do not exist in JSON file: '{json_data}'")
            json_data.get(key_name).append(new_data)
            utils_logger.debug(f"Appending new data '{new_data}' to list of dicts: '{json_data.get(key_name)}'")
            return json_data
