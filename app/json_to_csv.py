import json
import csv

def convert_json_to_csv(json_file_path, csv_file_path):
    try:
        with open(json_file_path, 'r') as file:
            # Parse the JSON data
            data = json.load(file)

        # Check if data is a list of dictionaries
        if not all(isinstance(item, dict) for item in data):
            raise ValueError("JSON data is not formatted as a list of dictionaries")

        # Write to a CSV file
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            for row in data:
                writer.writerow(row)

        print(f"JSON data has been successfully written to {csv_file_path}")

    except FileNotFoundError:
        print(f"File {json_file_path} not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON.")
    except ValueError as e:
        print(e)


