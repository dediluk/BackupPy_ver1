

import os
import time
import zipfile

target_dir = 'D:\\backups'
backup_folder_name = target_dir + os.sep + time.strftime("%Y%m%d")      #âñå áýêàïû çà îäèí äåíü õðàíÿòñÿ â îäíîé ïàïêå

if not os.path.exists(backup_folder_name):
    os.mkdir(backup_folder_name)
    print("Êàòàëîã {0} óñïåøíî ñîçäàí!".format(backup_folder_name))

while True:
    source = input("Ââåäèòå ïóòü:")                                     #ïóòü ê ïàïêå/ôàéëó, êîòîðûå íàäî çààðõèâèðîâàòü

    if not os.path.isdir(source):
        print("Îøèáêà. Ïîïðîáóéòå ñíîâà!")
        continue

    user_comment = input("Ââåäèòå êîììåíòàðèé ê àðõèâó:")               #êîììåíòàðèé ê íàçâàíèþ ôàéëà

    if user_comment == 0:                                               #äîáàâëåíèå êîììåíòàðèÿ, åñëè îí åñòü
        target = backup_folder_name + os.sep + time.strftime('%H%M') + '.zip'
    else:
        target = backup_folder_name + os.sep + time.strftime('%H%M') + "_" + user_comment.replace(" ", "_")  +'.zip'

    try:                                                                #ñîçäàíèå àðõèâà è çàïèñü ôàéëîâ â íåãî
        zip_backup = zipfile.ZipFile(target, 'w')
        time_before = time.time()
        for root, dirs, files in os.walk(source):
            for file in files:
                zip_backup.write(os.path.join(root, file))
        print("Àðõèâ ñîçäàí â {0} çà {1} ñåê".format(backup_folder_name, round(time.time() - time_before, 3)))
        break
    except:
        print("Îøèáêà. Ïîïðîáóéòå ñíîâà!")
