import process_images
import os
import shutil
import json


def load_config(file_path):
    try:
        with open(file_path, 'r') as file:
            config = json.load(file)
            return config
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {file_path}")
        return None

def move_zip_file(source_directory, file_name, processed_directory):
    # Construct the full path of the source and destination
    source_path = os.path.join(source_directory, file_name)
    destination_path = os.path.join(processed_directory, file_name)

    # Check if the source file exists
    if not os.path.exists(source_path):
        print(f"File not found: {source_path}")
        return False

    # Check if the processed directory exists, create if not
    if not os.path.exists(processed_directory):
        os.makedirs(processed_directory)

    # Move the file
    try:
        shutil.move(source_path, destination_path)
        print(f"File moved successfully from {source_path} to {destination_path}")
        return True
    except Exception as e:
        print(f"Error moving file: {e}")
        return False

def list_zip_files(source_directory):
    # List to hold the names of zip files
    zip_files = []

    # Check if the source directory exists
    if not os.path.exists(source_directory):
        print(f"Directory not found: {source_directory}")
        return zip_files

    # Iterate over the files in the source directory
    for file in os.listdir(source_directory):
        if file.endswith('.zip'):
            zip_files.append(file)

    return zip_files

if __name__ == "__main__":
    # Example usage
    config = load_config('config.json')
    source_dir = config['source_directory']
    processed_dir = config['processed_directory']
    output_dir = config['output_directory']
    temp_dir = config['temp_directory']
    source_file_names = list_zip_files(source_dir)
    for zip_file_name in source_file_names:
        process_images.process_images(f'{source_dir}/{zip_file_name}', output_dir, temp_dir)
        move_zip_file(source_dir, zip_file_name, processed_dir)











