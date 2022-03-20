#!/usr/bin/python3
from committer import *

if Committer().cmt_num == 0:
    rnd = Committer().cmt_range
    print(f"total commits: {rnd}")
    for i in range(rnd):
        Committer().commit()

