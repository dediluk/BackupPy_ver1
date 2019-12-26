import os
import time
import zipfile

target_dir = 'D:\\backups'
backup_folder_name = target_dir + os.sep + time.strftime("%Y%m%d")      #все бэкапы за один день хранятся в одной папке

if not os.path.exists(backup_folder_name):
    os.mkdir(backup_folder_name)
    print("Каталог {} успешно создан!".format(backup_folder_name))

while True:
    source = input("Введите путь:")                                     #путь до файла/папки, которые хотим заархивировать

    if not os.path.isdir(source):
        print("Данного каталога не существует! Попробуйте снова")
        continue

    user_comment = input("Введите свой комментарий к архиву:")          #комментарий добавляется к названию архива

    if user_comment == 0:                                               #добавление комментария, если он существует
        target = backup_folder_name + os.sep + time.strftime('%H%M') + '.zip'
    else:
        target = backup_folder_name + os.sep + time.strftime('%H%M') + "_" + user_comment.replace(" ", "_")  +'.zip'

    try:                                                                #создание архива и запись файлов в него
        zip_backup = zipfile.ZipFile(target, 'w')
        time_before = time.time()
        for root, dirs, files in os.walk(source):
            for file in files:
                zip_backup.write(os.path.join(root, file))
        print("Архив успешно создан в {0} за {1} сек".format(backup_folder_name, round(time.time() - time_before, 3)))
        break
    except:
        print("Ошибка! Попробуйте снова")
