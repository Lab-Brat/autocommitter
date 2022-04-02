import re
import os
import datetime
from pprint import pprint

inp = 'input.txt'

class decoder():
    def __init__(self, inp):
        self.inp = inp
        self.inp_data = []
        self.star_dic = {}

    def read_inp(self):
        '''
        read the input file and
        create a list of the values by column
        '''
        with open(self.inp, 'r') as f:
            data = f.readlines()
        [self.inp_data.append(line[:-1]) for line in data]

    def read_block(self, week_stars, wn):
        '''
        translate the values from inp_data into dates
        '''
        star_count = 0
        commit_days = []
        now = datetime.datetime.now()
        days_til_sunday = 6 - now.weekday()
        for i, star in enumerate(week_stars):
            if star == '*':
                d = days_til_sunday + i + (wn*7)
                raw = now + datetime.timedelta(days=d)
                # check if it's the first commit
                if star_count == 0:
                    commit_date = f'{raw.year}-{raw.month}-{raw.day}'
                elif star_count != 0:
                    # check if a new year or month has started
                    if int(commit_date[0:4]) == raw.year and \
                       int(commit_date[5])   == raw.month:
                           commit_date += f',{raw.day}'
                    else:
                        commit_days.append(commit_date)
                        commit_date = f'{raw.year}-{raw.month}-{raw.day}'
                star_count += 1
        commit_days.append(commit_date) 
        return commit_days

    def get_star(self):
        '''
        create a dictionary of the format {week#: commit_days}
        '''
        self.read_inp()
        for i in range(len(self.inp_data[0])):
            week_stars = [j[i] for j in self.inp_data]
            self.star_dic[f'week{i+1}'] = self.read_block(week_stars, i)
        return self.star_dic


if __name__ == '__main__':
    dc = decoder(inp)
    star_dict = dc.get_star()
    pprint(star_dict)

