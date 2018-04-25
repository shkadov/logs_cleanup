import zipfile
import os
import fnmatch
import time

old_date       = 1                                # Get min files age
file_path      = ''                                 # Get logs folder
current_time   = time.time()                        # Get current time


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
                    if file_age > old_date:
                        zipfilename = file_name + '.zip'
                        file_zip = zipfile.ZipFile(zipfilename, 'w')
                        file_zip.write(file_name, compress_type=compression)
                        file_zip.close()
                        os.remove(file_name)



    except Exception:
        print("Error")

# Check if folder exists
def folder_exist(file_path):
    try:
        os.stat(file_path)
    except Exception:
        print ("Folder is not exist")
        return

folder_exist(file_path)
zipping_file(file_path)