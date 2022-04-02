#!/usr/bin/python3
from committer import *

if Committer().cmt_num == 0:
    '''
    if there are no commits done in a day,
    run the committer rnd times
    '''
    rnd = Committer().cmt_range
    print(f"total commits: {rnd}")
    for i in range(rnd):
        Committer().commit()

