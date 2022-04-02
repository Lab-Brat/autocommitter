import os
import random
import logging
import subprocess
from patt import pattern


class Committer():
    def __init__(self):
        self.x = 1
        self.cmt_range = random.randint(1, 2)
        self.cron_patt = pattern(self.x).gen_cron()
        self.sed_patt = pattern(self.x).mod_timer()

        self.gucmd = 'git config --list | grep user.name | sed "s/user.name=//g"'
        self.gituser = subprocess.getoutput(self.gucmd)
        self.git_path = "/home/$USER/autocommitter"
        self.git_comment = "'cmt.sh add entry to tmp_file'"
        self.cmt_cmd = f"git -C {self.git_path} rev-list HEAD \
                         --author={self.gituser} --since '00:00' --count"
        self.cmt_num = int(subprocess.getoutput(self.cmt_cmd))

        logging.basicConfig(level=logging.INFO)

    def add_cron(self):
        '''
        pass patt.py generated crontab to users cron
        '''
        cmd = f"echo '{self.cron_patt}' | crontab"
        os.system(cmd)
        # print(cmd)
        logging.log(logging.INFO, "[CRONTAB ADDED]")

    def add_timer(self):
        '''
        add systemd timer
        '''
        os.system(self.sed_patt)
        os.system('systemctl --user daemon-reload')
        logging.log(logging.INFO, "[TIMER MODIFIED]")

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
