#!/usr/bin/python3
import os
from committer import *

cmt = Committer()
cmt.add_timer()
os.system(f'systemctl start --user committer.service')

