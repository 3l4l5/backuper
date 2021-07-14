import subprocess
import json, os, sys
import datetime

DIR_INFO = os.path.join("dir_info.json")

json_open = open(DIR_INFO, 'r')
json_load = json.load(json_open)

save_dir = json_load["save_dir"]
backup_list = json_load["backup_list"]

for backup in backup_list:
    filename = str(datetime.datetime.now()).replace("-", "").replace(" ", "").replace(":", "").split(".")[0]
    save_dir_name = os.path.join(save_dir, backup["path"].split("/")[-1], )

    os.mkdir(os.path.join(save_dir_name,filename))
    subprocess.run(["scp", "-r", backup["cliant"]+":"+backup["path"], os.path.join(save_dir_name,filename)])