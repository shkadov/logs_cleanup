import os, logging

# Check if log file exists

def log_file_exist(log_file):
    try:
        if not os.path.exists(log_file):
            file(log_file,'w').close()
    except Exception as e:
        logging.error(str(e))
