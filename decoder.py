import re
import os

inp = 'input.txt'

class decoder():
    def __init__(self, inp):
        self.inp = inp
        self.inp_data = []

    def read_inp(self):
        with open(self.inp, 'r') as f:
            data = f.readlines()

        [self.inp_data.append(line[:-1]) for line in data]

if __name__ == '__main__':
    dc = decoder(inp)
    dc.read_inp()
    print(dc.inp_data)
