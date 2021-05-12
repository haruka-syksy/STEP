from collections import Counter

def score_sort(dictionary):
    for i in range(len(dictionary)):
        max_index = i
        for j in range(i+1, len(dictionary)):
            if dictionary[max_index][2] < dictionary[j][2]:
                max_index = j
        dictionary[max_index], dictionary[i] = dictionary[i], dictionary[max_index]

        print(i)
        print(dictionary[i])
    return dictionary

def count_word(word):
    #出てきた文字の回数を数値の配列にする
    #catなら、'abcdefghijklmnopqrstuvwsyz'->[1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]

    #単語に出てくるアルファベットの数を調べる
    count_num = sorted(list(Counter(word).items()))

    alphabet = 'abcdefghijklmnopqrstuvwxyz'#26個
    count_array = [0]*26
    for i in range(len(count_num)):
        index = alphabet.find(count_num[i][0])
        count_array[index] += count_num[i][1]
    return count_array

def score(counting):
    sum = 0
    for i in range(len(counting)):
        if i in [9, 10, 16, 23, 25]:
            #j, k, g, x, z
            if counting[i] > 0:
                sum += counting[i] + 3*counting[i]

        elif i in [1, 5, 6, 15, 21, 22, 24]:
            #b, f, g, p, v, w, y
            if counting[i] > 0:
                sum += counting[i] + 2*counting[i]
        elif i in [2, 3, 11, 12, 20]:
            #c, d, l, m, u
            if counting[i] > 0:
                sum += counting[i] + 1*counting[i]
        else:
            sum += counting[i]
    return sum

def make_new_dictionary(dictionary):
    #(文字のカウント, 元の単語)のペアを作って新しい辞書を作る
    new_dictionary = []

    for i in range(len(dictionary)):
        counting = count_word(dictionary[i])
        score_num = score(counting)
        count_ch = list(map(str,counting))
        count_str = count_ch[0]
        for j in range(1,len(count_ch)):
            count_str += "," + count_ch[j]
        #count_str = ''.join(count_ch)
        new_dictionary.append((count_str, dictionary[i], score_num))

    sorted_dictionary = score_sort(new_dictionary)

    return sorted_dictionary

if __name__=='__main__':
    f1 = open('words.txt', 'r')
    data = f1.read()
    f1.close()
    dictionary = data.split() #\nを除いて配列にする

    new_dictionary = []
    new_dictionary = make_new_dictionary(dictionary)
    #print(new_dictionary)

    f2 = open('score_sort_dictionary2.txt', 'w')
    for word in new_dictionary:
        print(*word, sep=',', file=f2)
    f2.close()
