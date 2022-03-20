import os
import re
import subprocess
import datetime as dt


class pattern():
    def __init__(self, x):
        self.x = x
        self.date = str(dt.datetime.now())
        self.year = self.date[0:4]
        self.month = int(self.date[5:7])
        self.day = int(self.date[8:10])
        self.hour = int(self.date[11:13])
        self.min = int(self.date[14:16])

        self.path_cmt = subprocess.getoutput(f'readlink -f cmt.py')
        self.path_tim = '/home/$USER/.config/systemd/user'

        self.days = ','.join([f'{self.day+i}' for i in range(x)])

    def gen_cron(self, show=False):
        tm = f'{self.min+1} {self.hour} {self.days} {self.month} * '
        cmd = f'/usr/bin/python3 {self.path_cmt} &> /home/lab-brat/cron.log'
        crontab = tm + cmd
        
        if show == True:
            print(crontab)

        return crontab

    def gen_timer(self, show=False):
        #add timer and service checker
        da = f'{self.year}-{self.month}-{self.days} {self.hour}:{self.min+1}:00'
        sed = f'sed -i "s/OnCalendar=.*/OnCalendar={da}/" {self.path_tim}/committer.timer'
        
        if show == True:
            print(sed)

        return sed
        

if __name__ == "__main__":
    x = 1
    pattern(x).gen_cron(show=True)

