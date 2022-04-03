#!/usr/bin/python3
import os
from committer import *

# add systemd service and timer
cmt = Committer()
cmt.add_timer()
# os.system(f'systemctl --user daemon-reload')
# os.system(f'systemctl --user start committer.service')

