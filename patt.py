import os
import configparser
import datetime as dt
from decoder import *
from pprint import pprint

class pattern():
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config')
        self.username = config['USER']['username']
        self.home_path = config['USER']['home_path']
        self.repo_path = config['USER']['repo_path']

        self.date = str(dt.datetime.now())
        self.year = self.date[0:4]
        self.month = int(self.date[5:7])
        self.day = int(self.date[8:10])
        self.hour = int(self.date[11:13])
        self.min = int(self.date[14:16])

        self.path_cmt = f'{self.repo_path}/cmt.py'
        self.path_tim = f'{self.home_path}/.config/systemd/user'

        self.days = ','.join([f'{self.day+i}' for i in range(1)])
        self.stars = decoder('input.txt').get_star()


    def gen_service(self, show=False):
        '''
        create a user systemd service file
        '''
        os.system(f'mkdir -p {self.path_tim}')
        with open(f'{self.path_tim}/committer.service', 'w') as srv:
            srv.write('[Unit]\n')
            srv.write('Description=autocommiter github project\n')
            srv.write('Wants=autocommiter.timer\n\n')
            srv.write('[Service]\n')
            srv.write('Type=simple\n')
            srv.write(f'ExecStart={self.path_cmt}\n\n')
            srv.write('[Install]\n')
            srv.write('WantedBy=multi-user.target\n')
            srv.truncate()

    def list_stars(self):
        '''
        reads dictionary with date values 
        and splits everything to separate strings
        '''
        self.split_stars = []
        for s in self.stars:
            for i in self.stars[s]:
                self.split_stars.append(i)

    def gen_timer(self, show=False):
        '''
        create a user systemd timer file
        '''
        self.list_stars()
        with open(f'{self.path_tim}/committer.timer', 'w') as tmr:
            tmr.write('[Unit]\n')
            tmr.write('Description=autocommiter github project\n')
            tmr.write('Requires=autocommiter.service\n\n')
            tmr.write('[Timer]\n')
            tmr.write('Unit=autocommiter.service\n')
            for line in self.split_stars:
                tmr.write(f'OnCalendar={line} 12:00:00\n')
            tmr.write('\n')
            tmr.write('[Install]\n')
            tmr.write('WantedBy=timers.target\n')
            tmr.truncate()

    def mod_timer(self, show=False):
        '''
        generates a sed command to replace 
        the value of OnCalendar in the timer file
        '''
        da = f'{self.year}-{self.month}-{self.days} {self.hour}:{self.min+1}:00'
        sed = f'sed -i "s/OnCalendar=.*/OnCalendar={da}/" {self.path_tim}/committer.timer'

        if show == True: print(sed)
        return sed
        

if __name__ == "__main__":
    # pattern().mod_timer(show=True)
    # pattern().gen_service()
    # pattern().gen_timer()
    print(pattern().username)

