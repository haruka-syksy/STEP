#!/usr/bin/env python3

import sys
import time

from common import format_tour, read_input

import greedy_2opt
import greedy_2opt_start
import greedy_2opt_center

CHALLENGES = 7

def generate_sample_output(filename):
    list = [(greedy_2opt, 'greedy_2opt'), (greedy_2opt_start, 'greedy_2opt_start'), (greedy_2opt_center, 'greedy_2opt_center')]

    for i in range(len(list)):
        if filename == list[i][1]:
            solver = list[i][0]

    for i in range(CHALLENGES):
        cities = read_input(f'input_{i}.csv')
        tour = solver.solve(cities)
        with open(f'output_{i}.csv', 'w') as f:
            f.write(format_tour(tour) + '\n')

if __name__ == '__main__':
    assert len(sys.argv) > 1
    #start = time.time()
    generate_sample_output(sys.argv[1])
    #elapsed_time = time.time() - start
    #print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
