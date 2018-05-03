# Zipping log files function
import fnmatch
import os
import zipfile
import logging
import datetime
from os.path import basename
from logs_cleanup import current_time, old_date, log_file

try:
    import zlib
    compression = zipfile.ZIP_DEFLATED
except:
    compression = zipfile.ZIP_STORED

modes = { zipfile.ZIP_DEFLATED: 'deflated',
          zipfile.ZIP_STORED: 'stored',
          }

def zipping_file(file_path):
    global old_date
    try:
        for dir, subdir, files in os.walk(file_path):
            for file in files:
                file_name = os.path.join(dir, file)
                file_date = os.path.getmtime(file_name)
                file_age = (int(current_time) - int(file_date)) / 86400 # get current file age
                old_date = int(old_date)
                if fnmatch.fnmatch(file_name, '*[!.zip]'):
                    if file_age > old_date:
                        zipfilename = file_name + '.zip'
                        file_zip = zipfile.ZipFile(zipfilename, 'w')
                        file_zip.write(file_name, basename(file_name), compress_type=compression)
                        with open(log_file, 'a') as f:
                            f.write(str(datetime.datetime.now()) + ' File ' + str(file_name) + ' has been compressed\n')
                            f.close()
                        file_zip.close()
                        os.remove(file_name)




    except BaseException as e:
        logging.error(str(e))