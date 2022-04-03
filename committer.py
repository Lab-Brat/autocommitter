import os
import random
import logging
import subprocess
from patt import pattern


class Committer():
    def __init__(self):
        self.cmt_range = random.randint(1, 2)
        self.patt = pattern()
        self.sed_patt = self.patt.mod_timer()

        self.gucmd = 'git config --list | grep user.name | sed "s/user.name=//g"'
        self.gituser = subprocess.getoutput(self.gucmd)
        self.git_path = self.patt.repo_path
        self.git_comment = "'cmt.sh add entry to tmp_file'"
        self.cmt_cmd = f"git -C {self.git_path} rev-list HEAD \
                         --author={self.gituser} --since '00:00' --count"
        self.cmt_num = int(subprocess.getoutput(self.cmt_cmd))

        logging.basicConfig(level=logging.INFO)

    def add_timer(self):
        '''
        add systemd timer
        '''
        self.patt.gen_timer()
        logging.log(logging.INFO, "[TIMER ADDED]")

    def mod_tmp(self):
        '''
        action performed by cmt.py
        '''
        os.system(f"echo $(date) >> {self.git_path}/tmp/tmp_file")

    def commit(self):
        '''
        preform git add, commit and push
        '''
        self.mod_tmp()
        git_add = f"git -C {self.git_path} add tmp/tmp_file"
        git_com = f"git -C {self.git_path} commit -m {self.git_comment} -q"
        git_push = f"git -C {self.git_path} push --quiet"

        os.system(git_add)
        os.system(git_com)
        os.system(git_push)
        logging.log(logging.INFO, '[COMMITTED]')


if __name__ == "__main__":
    Committer().add_timer()
    # Committer().commit()

