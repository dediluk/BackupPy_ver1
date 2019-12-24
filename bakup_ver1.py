import os
import time
import zipfile

target_dir = 'D:\\backups'

while True:
    source = input("Input path:")
    if not os.path.isdir(source):
        print("Fail. Try again")
        continue

    target = target_dir + os.sep + time.strftime('%Y%m%d%H%M') + '.zip'
    try:
        zip_backup = zipfile.ZipFile(target, 'w')

        for root, dirs, files in os.walk(source):
            for file in files:
                zip_backup.write(os.path.join(root, file))
        print("Zip is ready at ", target_dir)
        break
    except:
        print("Failure. Try again")
