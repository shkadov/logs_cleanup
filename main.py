import time
import ConfigParser
import datetime
from log_file_exists_check import log_file_exist
from folder_exists_check import folder_exist
import zipping

settings_file = ConfigParser.ConfigParser()
settings_file.read('settings.ini')

old_date = settings_file.get('vars', 'old_date')
file_path = settings_file.get('vars', 'folder')
log_file = settings_file.get('vars', 'logfile')
current_time   = time.time()                      # Get current time

def main():
    log_file_exist(log_file)
    print("Started: " + str(datetime.datetime.now()))
    print("==========================================")
    folder_exist(file_path)
    zipping.zipping_file(file_path)
    print("==========================================")
    print("Finished: " + str(datetime.datetime.now()))

if __name__ == "__main__":
    main()