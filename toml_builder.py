# DO NOT USE

import toml
import os

config_data = {
    "title": "PythonSimpleFunctions",
    "version": "1.0.0"
}

file_path = "pyproject.toml"

try:
    with open(file_path, "w") as f:
        toml.dump(config_data, f)
    print(f"TOML file '{file_path}' created successfully.")
except IOError as e:
    print(f"Error creating file: {e}")

if os.path.exists(file_path):
    with open(file_path, "r") as f:
        print("\nFile content:")
        print(f.read())