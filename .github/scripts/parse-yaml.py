import os
import sys
import yaml

chall_dir = sys.argv[1]

def is_valid_challenge_yaml(yaml_file):
    base_dir = os.path.dirname(os.path.realpath(yaml_file))
    required_keys = set(['name', 'author', 'category', 'description', 'flags', 'attribution', 'value', 'type', 'image', 'protocol', 'host'])

    with open(yaml_file, 'r') as stream:
        try:
            chall_dict = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print("Error parsing YAML:", exc)
            return False

    actual_keys = set(chall_dict.keys())

    if not required_keys.issubset(actual_keys):
        return False

    if chall_dict["image"] is not None and not os.path.isfile(base_dir + "/Dockerfile"):
        print("Dockerfile not found!")
        return False

    return True

def has_correct_folders(chall_dir):
    return os.path.isdir(chall_dir + "/src") and os.path.isdir(chall_dir + '/solve') and os.path.isfile(chall_dir + '/challenge.yaml') 

print(chall_dir)
assert has_correct_folders(chall_dir), f"{chall_dir} does not have the right folders and files"
assert is_valid_challenge_yaml(chall_dir + '/challenge.yaml'), f"{chall_dir} has an invalid challenge.yaml file"