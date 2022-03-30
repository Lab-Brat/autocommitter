import re
import os
import pprint
import datetime

inp = 'input.txt'

class decoder():
    def __init__(self, inp):
        self.inp = inp
        self.inp_data = []
        self.star_dic = {}

    def read_inp(self):
        with open(self.inp, 'r') as f:
            data = f.readlines()

        [self.inp_data.append(line[:-1]) for line in data]

    def read_block(self, week_stars, wn):
        commit_days = []
        now = datetime.datetime.now()
        days_til_sunday = 6 - now.weekday()
        for i, star in enumerate(week_stars):
            if star == '*':
                d = days_til_sunday + i + (wn*7)
                raw = now + datetime.timedelta(days=d)
                commit_date = f'{raw.year}-{raw.month}-{raw.day}'
                commit_days.append(commit_date)
        return commit_days


    def get_star(self):
        self.read_inp()
        for i in range(len(self.inp_data[0])):
            week_stars = [j[i] for j in self.inp_data]
            self.star_dic[f'week{i+1}'] = self.read_block(week_stars, i)
        pprint.pprint(self.star_dic)

if __name__ == '__main__':
    dc = decoder(inp)
    dc.get_star()

