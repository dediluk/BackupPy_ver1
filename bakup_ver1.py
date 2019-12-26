# coding=windows-1251

import os
import time
import zipfile

target_dir = 'D:\\backups'
backup_folder_name = target_dir + os.sep + time.strftime("%Y%m%d")      #��� ������ �� ���� ���� �������� � ����� �����

if not os.path.exists(backup_folder_name):
    os.mkdir(backup_folder_name)
    print("������� {0} ������� ������!".format(backup_folder_name))

while True:
    source = input("������� ����:")                                     #���� � �����/�����, ������� ���� ��������������

    if not os.path.isdir(source):
        print("������. ���������� �����!")
        continue

    user_comment = input("������� ����������� � ������:")               #����������� � �������� �����

    if user_comment == 0:                                               #���������� �����������, ���� �� ����
        target = backup_folder_name + os.sep + time.strftime('%H%M') + '.zip'
    else:
        target = backup_folder_name + os.sep + time.strftime('%H%M') + "_" + user_comment.replace(" ", "_")  +'.zip'

    try:                                                                #�������� ������ � ������ ������ � ����
        zip_backup = zipfile.ZipFile(target, 'w')
        time_before = time.time()
        for root, dirs, files in os.walk(source):
            for file in files:
                zip_backup.write(os.path.join(root, file))
        print("����� ������ � {0} �� {1} ���".format(backup_folder_name, round(time.time() - time_before, 3)))
        break
    except:
        print("������. ���������� �����!")
