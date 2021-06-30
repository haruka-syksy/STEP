#!/usr/bin/env python3

#4分割, 欲張り法, 2opt

import sys
import math
import time

#ファイル読み込み
def read_input(filename):
    with open(filename) as f:
        cities = []
        i = 0
        for line in f.readlines()[1:]:  # Ignore the first line.
            xy = line.split(',')
            cities.append((i, (float(xy[0]), float(xy[1]))))
            i += 1
        return cities

#書き出しのためのフォーマット
def format_tour(tour):
    return 'index\n' + '\n'.join(map(str, tour))

#距離を求める
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

#欲張り法
def greedy(cities, N, dist, start_index):
    current_city = start_index
    unvisited_cities = set(range(0, N))
    unvisited_cities.remove(start_index)
    tour = [current_city]

    while unvisited_cities:
        next_city = min(unvisited_cities,
                        key=lambda city: dist[current_city][city])
        unvisited_cities.remove(next_city)
        tour.append(next_city)
        current_city = next_city
    return tour

#2-opt法
def two_opt(tour, N, dist):
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
                    l1 = dist[tour[i]][tour[i1]]
                    l2 = dist[tour[j]][tour[j1]]
                    l3 = dist[tour[i]][tour[j]]
                    l4 = dist[tour[i1]][tour[j1]]
                    if l1 + l2 > l3 + l4: #今までの辺よりも短ければつなぎ変える
                        new_path = tour[i1:j+1] #変更する点を抜き出す
                        tour[i1:j+1] = new_path[::-1] #逆順に挿入する
                        swap_bool += 1
        if swap_bool == 0:
             break #入れ替わりが起きなければ終了
    return tour

#4つに領域分割
def divide(cities):
    N = len(cities) #場所の数
    max_x = cities[0][1][0] #xの最大値
    min_x = cities[0][1][0] #xの最小値
    max_y = cities[0][1][1] #yの最大値
    min_y = cities[0][1][1] #yの最小値

    #x, yの最大値最小値を求める
    for i in range(N):
        if max_x < cities[i][1][0]:
            max_x = cities[i][1][0]
        if min_x > cities[i][1][0]:
            min_x = cities[i][1][0]
        if max_y < cities[i][1][1]:
            max_y = cities[i][1][1]
        if min_y > cities[i][1][1]:
            min_y = cities[i][1][1]

    #中央値を求める
    mid_x = (min_x + max_x)/2.0
    mid_y = (min_y + max_y)/2.0

    cities1 = []
    cities2 = []
    cities3 = []
    cities4 = []

    #4分割したい
    for i in range(N):
        if cities[i][1][0] <= mid_x and cities[i][1][1] <= mid_y:
            cities1.append(cities[i])
        elif cities[i][1][0] > mid_x and cities[i][1][1] < mid_y:
            cities2.append(cities[i])
        elif cities[i][1][0] >= mid_x and cities[i][1][1] >= mid_y:
            cities3.append(cities[i])
        else:
            cities4.append(cities[i])

    div_cities = []
    div_cities.append(cities1)
    div_cities.append(cities2)
    div_cities.append(cities3)
    div_cities.append(cities4)

    return div_cities


#領域全体に2opt法を施す
def two_opt_to_all(cities, tour):
    N = len(cities) #場所の数

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(i, N):
            dist[i][j] = dist[j][i] = distance(cities[i][1], cities[j][1])

    #g_tour = greedy(cities, N, dist)
    two_opt_tour = two_opt(tour, N, dist)

    return two_opt_tour

def solve(city):
    #4つに分割
    cities = divide(city)
    min_index = 0
    tour = []

    #4つの領域それぞれの経路を求める
    for div_index in range(4):
        N = len(cities[div_index]) #場所の数

        #座標が一つしかなかったら終わり
        if N == 1:
            tour.extend([cities[div_index][0][0]])
            continue;

        dist = [[0] * N for i in range(N)]
        for i in range(N):
            for j in range(i, N):
                dist[i][j] = dist[j][i] = distance(cities[div_index][i][1], cities[div_index][j][1])

        g_tour = greedy(cities[div_index], N, dist, min_index)
        #print("g_tour", g_tour)
        two_opt_tour = two_opt(g_tour, N, dist)
        #print("two_opt_tour", two_opt_tour)

        if div_index < 3:
            #今の領域の経路の最後に一番近い点を次の分割の点から見つける
            min_index = 0
            min_dist = distance(cities[div_index][two_opt_tour[N-1]][1], cities[div_index+1][0][1])
            for i in range(1, len(cities[div_index+1])):
                tmp_dist = distance(cities[div_index][two_opt_tour[N-1]][1], cities[div_index+1][i][1])
                if min_dist > tmp_dist:
                    min_index = i
                    min_dist = tmp_dist

        #今の領域の経路を決定
        tmp_tour = []
        for i in range(N):
            tmp_tour.append(cities[div_index][two_opt_tour[i]][0])
        #全体の経路に結合
        tour.extend(tmp_tour)

    #全体の経路に2-opt法を施す
    new_tour = two_opt_to_all(city, tour)

    return new_tour


if __name__ == '__main__':

    for i in range(8):
        start = time.time()
        cities = read_input(f'input_{i}.csv')
        tour = solve(cities)
        with open(f'output_{i}.csv', 'w') as f:
            f.write(format_tour(tour) + '\n')
        end = time.time()
        print ("input", i, " time: %.6f sec" % (end - start))

    '''
    #1データだけ実行する場合
    assert len(sys.argv) > 1
    begin = time.time()

    tour = solve(read_input(sys.argv[1]))

    print(format_tour(tour))
    end = time.time()
    print("time: %.6f sec" % (end - begin))
    '''
