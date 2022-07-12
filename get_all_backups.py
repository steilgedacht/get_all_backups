 
from ftplib import FTP
import os
import json
from tqdm import tqdm

# load server data
with open('server.json') as f:
    servers = json.load(f)

os.makedirs("backups", exist_ok=True)
p_bar=tqdm(total=len(servers),desc="loading")
log = "Logging of backups \n"

# iterate over all server entries in the json file and get every backup
for server in servers:
    hostname = servers[server]["hostname"]
    username = servers[server]["username"]
    password = servers[server]["password"]
    prefix = servers[server]["root"]

    if hostname == '' or username == '' or password == '' or prefix == '':
        log += f"Server {server}: incomplete data\n"
        continue

    try:
        ftp = FTP(hostname, username, password)
    except:
        log += f"Server {server}: wrong data\n"
        continue

    ftp.cwd(prefix + '/administrator/components/com_akeeba/backup')

    # get all the files in the backup directory
    folder_files = []
    try:     
        ftp.dir(folder_files.append)
    except:
        log += f"Server {server}: wrong root\n"
        continue

    # filter out the backup files 
    backups = []
    for file in folder_files:
        file_metadata = file.split(' ')
        file_metadata = [s for s in file_metadata if s != '']
        if file_metadata[-1].endswith('.zip') or file_metadata[-1].endswith('.jpa'):
            backups.append(file_metadata[-1])
    
    if len(backups) == 0:
        log += f"Server {server}: wrong root\n"
        continue

    # sort backups by date and thake the latest backup
    backups.sort()
    backup = backups[-1]

    # download backup
    with open(os.path.join("backups", backup), 'wb') as f:
        ftp.retrbinary('RETR ' + backup, f.write)

    ftp.quit()

    # rename the downloaded backup
    os.rename(os.path.join("backups", backup),os.path.join("backups", server.replace(" ", "_") + "_" + backup))
    p_bar.update(1)

p_bar.close()

with open("log.txt", 'w') as f:
    f.write(log)