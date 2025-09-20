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
    jfile=json.load(f)
# 3. Load configuration files
#    - config.yaml → source/backup paths
#    - config.json → additional settings


logging.basicConfig(level=logging.INFO,
                        filename="logs/poclog.txt",
                        filemode="w",
                        format="%(asctime)s - %(levelname)s -%(message)s"
                        )

log = logging.getLogger(__name__) 
# 4. Setup logging
#    - log to logs/backup.log
#    - format with timestamp + log level

parser = argparse.ArgumentParser(description="Demo of the args for POC")
parser.add_argument( "--source" ,help="Source file name", default=yfile["source"])
parser.add_argument( "--dest" ,help="dest file name" ,default=jfile["backup"] )
parser.add_argument( "--verbose" ,action="store_true",help="Enable verbose mode" )
args=parser.parse_args()
# 5. Parse CLI arguments with argparse
#    - --source (source folder)
#    - --dest (backup folder)
#    - --verbose (flag)


if not os.path.exists(args.dest):
    os.makedirs(args.dest)

for file in os.listdir(args.source):
    src=os.path.join(args.source,file)
    dest=os.path.join(args.dest,f"{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}_{file}")
    if os.path.isfile(src):
        shutil.copy(src, dest)
        log.info(f"File {src} copied to {dest} successfull \n")
        if args.verbose:
            print(f"File {src} copied to {dest} successfull")

# 6. Perform backup
#    - check/create destination folder
#    - copy files with shutil
#    - use datetime to timestamp file names
#    - log each operation
#    - print if verbose


sp=subprocess.run(["ls"],capture_output=True, text=True)
log.info("THE OUTPUT OF THE SUBPROCESS IS  \n" + sp.stdout)
# 7. Run a system command (subprocess)
#    - e.g. "ls -l" or "dir"
#    - capture and log the output



payload={
    "status": "Backup successfull",
    "Files": os.listdir(args.dest)
}
# headers = {"Authorization": f"Bearer {API_KEY}"}
# r=requests.post("https://httpbin.org/post", payload=payload, headers=headers)
# log.info(f"API Response: {r.status_code}")
# 8. Send backup report to API (requests)
#    - payload with status, file list, sys info
#    - headers include API_KEY from dotenv
#    - log response status

print("Backup finished. Logs saved in logs/backup.log")
# 9. Exit
#    - print "Backup completed"
#    - close resources (ssh/ftp if extended in future)


