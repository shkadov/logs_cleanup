import zipfile
import os
import fnmatch
import time
import ConfigParser
import logging
import datetime

settings_file = ConfigParser.ConfigParser()
settings_file.read('settings.txt')

old_date = settings_file.get('vars', 'old_date')
file_path = settings_file.get('vars', 'folder')
log_file = settings_file.get('vars', 'logfile')
current_time   = time.time()                      # Get current time


try:
    import zlib
    compression = zipfile.ZIP_DEFLATED
except:
    compression = zipfile.ZIP_STORED

modes = { zipfile.ZIP_DEFLATED: 'deflated',
          zipfile.ZIP_STORED: 'stored',
          }

# Zipping log files function
def zipping_file(file_path):
    #global old_date, file_path, current_time
    try:
        for dir, subdir, files in os.walk(file_path):
            for file in files:
                file_name = os.path.join(dir, file)
                file_date = os.path.getmtime(file_name)
                file_age = (int(current_time) - int(file_date)) / 86400 # get current file age
                if fnmatch.fnmatch(file_name, '*[!.zip]'):
                    if file_age < old_date:
                        zipfilename = file_name + '.zip'
                        file_zip = zipfile.ZipFile(zipfilename, 'w')
                        file_zip.write(file_name, compress_type=compression)
                        with open(log_file, 'a') as f:
                            f.write(str(datetime.datetime.now()) + ' File ' + str(file_name) + ' has been compressed\n')
                            f.close()
                        file_zip.close()
                        os.remove(file_name)



    except BaseException as e:
        logging.error(str(e))

# Check if folder exists
def folder_exist(file_path):
    try:
        os.stat(file_path)
    except Exception as e:
        logging.error(str(e))
        return

def log_file_exist(log_file):
    try:
        if not os.path.exists(log_file):
            file(log_file,'w').close()
    except Exception as e:
        logging.error(str(e))



def main():
    log_file_exist(log_file)
    print("Started: " + str(datetime.datetime.now()))
    print("==========================================")
    folder_exist(file_path)
    zipping_file(file_path)
    print("==========================================")
    print("Finished: " + str(datetime.datetime.now()))

if __name__ == "__main__":
    main()