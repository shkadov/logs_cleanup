import os, logging

# Check if folder exists

def folder_exist(file_path):
    try:
        os.stat(file_path)
    except Exception as e:
        logging.error(str(e))
        return