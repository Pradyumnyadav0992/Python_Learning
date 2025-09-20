# 1. Imports
import os
import sys
import shutil
import subprocess
import logging
import json
import yaml
import requests
import argparse
import datetime
from dotenv import load_dotenv


load_dotenv()
API_KEY=os.getenv("API_KEY")
# 2. Load environment variables from .env
#    (API_KEY, DEBUG flag, etc.)

with open("config.yaml","r") as f:
    yfile=yaml.safe_load(f)

with open("config.json","r") as f:
    jfile=yaml.load(f)
# 3. Load configuration files
#    - config.yaml → source/backup paths
#    - config.json → additional settings


log=logging.basicConfig(level=logging.INFO,
                        filename=poclog.txt,
                        format="%(asctime)s - %(levelname)s -%(message)s"
                        )
# 4. Setup logging
#    - log to logs/backup.log
#    - format with timestamp + log level

parser = argparse.ArgumentParser(description="Demo of the args for POC")
parser.add_argument( "--source" ,help="Source file name", default=yfile["source"])
parser.add_argument( "--des" ,help="dest file name" ,default=yfile["backup"] )
parser.add_argument( "--verbose" ,action="store_true",help="Enable verbose mode" )
args=parser.parse_args()
# 5. Parse CLI arguments with argparse
#    - --source (source folder)
#    - --dest (backup folder)
#    - --verbose (flag)


if not os.path.exists(args.des):
    os.makedirs(args.des)

for file in os.listdir(args.source):
    src=os.path.join(args.source,file)
    date=datetime.datetime.now.strftime('%Y%m%d_%H%M%S')
    dest=os.path.join(args.des,{date}_file)
    if os.path.isfile(src):
        shutil.copy(src, dest)
        log.info(f"File {src} copied to {dest} successfulle")
        if args.verbose:
            print(f"File {src} copied to {dest} successfulle")

# 6. Perform backup
#    - check/create destination folder
#    - copy files with shutil
#    - use datetime to timestamp file names
#    - log each operation
#    - print if verbose


sp=subprocess.run(["ls","-l"],capture_output=True, text=True)
log.info(f"the output of the execute quar is {sp.stdout}")
# 7. Run a system command (subprocess)
#    - e.g. "ls -l" or "dir"
#    - capture and log the output



payload={
    "status": "Backup successfull"
    "Files":os.listdir(args.dest)
}
headers = {"Authorization": f"Bearer {API_KEY}"}
r=requests.post("https://httpbin.org/post", payload=payload, headers=headers)
log.info(f"API Response: {r.status_code}")
# 8. Send backup report to API (requests)
#    - payload with status, file list, sys info
#    - headers include API_KEY from dotenv
#    - log response status

print("Backup finished. Logs saved in logs/backup.log")
# 9. Exit
#    - print "Backup completed"
#    - close resources (ssh/ftp if extended in future)
