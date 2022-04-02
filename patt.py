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
        self.path_tim = '/home/labbrat/.config/systemd/user'

        self.days = ','.join([f'{self.day+i}' for i in range(x)])

    def gen_cron(self, show=False):
        tm = f'{self.min+1} {self.hour} {self.days} {self.month} * '
        cmd = f'/usr/bin/python3 {self.path_cmt} &> /home/lab-brat/cron.log'
        crontab = tm + cmd
        
        if show == True: print(crontab)
        return crontab

    def gen_service(self, show=False):
        os.system(f'mkdir -p {self.path_tim}')
        with open(f'{self.path_tim}/committer.service', 'w') as srv:
            srv.write('[Unit]\n')
            srv.write('Description=autocommiter github project\n')
            srv.write('Wants=autocommiter.timer\n\n')
            srv.write('[Service]\n')
            srv.write('Type=simple\n')
            srv.write('ExecStart=/home/boink/autocommitter/cmt.py\n\n')
            srv.write('[Install]\n')
            srv.write('WantedBy=multi-user.target\n')
            srv.truncate()

    def gen_timer(self, show=False):
        with open(f'{self.path_tim}/committer.timer', 'w') as tmr:
            tmr.write('[Unit]\n')
            tmr.write('Description=autocommiter github project\n')
            tmr.write('Requires=autocommiter.service\n\n')
            tmr.write('[Timer]\n')
            tmr.write('Unit=autocommiter.service\n')
            tmr.write('OnCalendar=\n\n')
            tmr.write('[Install]\n')
            tmr.write('WantedBy=timers.target\n')
            tmr.truncate()

    def mod_timer(self, show=False):
        da = f'{self.year}-{self.month}-{self.days} {self.hour}:{self.min+1}:00'
        sed = f'sed -i "s/OnCalendar=.*/OnCalendar={da}/" {self.path_tim}/committer.timer'

        if show == True: print(sed)
        return sed
        

if __name__ == "__main__":
    x = 1
    # pattern(x).mod_timer(show=True)
    pattern(x).gen_service()
    pattern(x).gen_timer()


