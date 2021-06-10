#!/usr/bin/env python3

#欲張り方と2-opt

import sys
import math

from common import print_tour, read_input

def distance(city1, city2): #距離を求める
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def greedy(cities, N, dist):#欲張り法
    current_city = 0
    unvisited_cities = set(range(1, N))
    tour = [current_city]

    while unvisited_cities:
        next_city = min(unvisited_cities,
                        key=lambda city: dist[current_city][city])
        unvisited_cities.remove(next_city)
        tour.append(next_city)
        current_city = next_city

    return tour

def two_opt(cities, N, dist): #2-optもどき
    while True:
        swap_bool = 0
        for i in range(1, N-2):
            i1 = i+1
            for j in range(i+2, N):
                if j == N-1:
                    j1 = 0
                else:
                    j1 = j + 1
                if i != 0 or j1 != 0:
                    l1 = dist[cities[i]][cities[i1]]
                    l2 = dist[cities[j]][cities[j1]]
                    l3 = dist[cities[i]][cities[j]]
                    l4 = dist[cities[i1]][cities[j1]]
                    if l1 + l2 > l3 + l4: #今までの辺よりも短ければつなぎ変える
                        new_path = cities[i1:j+1] #変更する点を抜き出す
                        cities[i1:j+1] = new_path[::-1] #逆順に挿入する
                        swap_bool += 1
        if swap_bool == 0:
             break #入れ替わりが起きなければ終了
    return cities


def solve(cities):
    N = len(cities) #場所の数

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(i, N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    g_tour = greedy(cities, N, dist)
    two_opt_tour = two_opt(g_tour, N, dist)

    return two_opt_tour


if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    print_tour(tour)
