#!/usr/bin/python3
import os
from committer import *

# add systemd service and timer
cmt = Committer()
cmt.add_service()
cmt.add_timer()
os.system(f'systemctl start --user committer.service')

