# midjourney_prompt_extractor
Scripts to extract prompts from a MidJourney ZIP archive file for generated images.

# Pre-requisites
* The code is tested with python 3.9. Please make sure your python version is atleast 3.9 . You must also have pip or similar installed
* install the 'pillow' module like so - pip install pillow

# How the script works
* The script reads from a directory containing zip files containing MJ generated images which contain metadata including the prompt.
* It extracts the images and places them in a temp directory before extracting the metadata.
* Once a zip file is processed it is moved to a 'processed' directory
* The metadata is placed in an 'output' directory.
* The metadata is extracted in 2 formats '.csv' (for spreadsheets) and '.json' for additional processing.
* The temp directory is not cleared of images - please clear manually

# How to run
* Pull from git or just download the files in tha 'app' directory to a suitable location.
* edit the config.json with a text editor for your local setup.
* ensure that your 'source', 'processed', 'output' and 'temp' directories exist.
* place the zip files to be processed in the source directory
* run the app.py
* once run the output will contain the extracted metadata in 2 file formats '.json' and '.csv' .



