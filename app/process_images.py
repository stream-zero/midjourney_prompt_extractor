import os
import json
import zipfile
from datetime import datetime
from PIL import Image
import json_to_csv

def unzip_file(zip_path, extract_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    return os.listdir(extract_path)  # Returns a list of extracted files

def process_image_metadata(image_path):
    with Image.open(image_path) as img:
        metadata = img.info.get("Description", "")
        parts = metadata.rsplit(" Job ID: ", 1)
        description = parts[0] if len(parts) > 1 else metadata
        job_id = parts[1] if len(parts) > 1 else None
        return description, job_id

def process_images(zip_path,output_dir):
    temp_dir = f"/tmp/{os.path.splitext(os.path.basename(zip_path))[0]}"
    os.makedirs(temp_dir, exist_ok=True)

    extracted_files = unzip_file(zip_path, temp_dir)
    image_data = []

    for file in extracted_files:
        if file.lower().endswith('.png'):
            file_path = os.path.join(temp_dir, file)
            description, job_id = process_image_metadata(file_path)
            image_data.append({
                "filename": file,
                "description": description,
                "job_id": job_id,
                "tags": [],  # Placeholder for tags
                "date": datetime.now().isoformat()
            })

    metadata_file = os.path.join(output_dir, f"{os.path.basename(zip_path).split('.')[0]}.json")
    with open(metadata_file, "w") as f:
        json.dump(image_data, f, indent=4)
        # Covert JSON to CSV
    json_to_csv.convert_json_to_csv(metadata_file, f"{metadata_file}.csv")



    # Clean up the temp directory if needed
    # os.rmdir(temp_dir)

