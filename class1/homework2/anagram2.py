from collections import Counter
import sys

def read_dictionary():
    #ソートしてある辞書を読み込む
    f = open('score_sort_dictionary.txt', 'r')
    data = f.read()
    f.close()

    list = data.split() #\nを除いて配列にする

    new = []

    for i in range(len(list)):#文字の出現回数と元の言葉をペアにする
        count_array = []
        l = list[i].split(',')
        for j in range(26):#文字の出現回数を数値の配列にする
            count_array.append(int(l[j]))
        new.append((count_array, l[26]))#l[26]は元の言葉
    return new

def read_textfile(fileName):
    #アナグラムを探すテキストファイル読み込み
    f = open(fileName, 'r')
    data = f.read()
    f.close()

    list = data.split() #\nを除いて配列にする

    return list

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



def linear_search(dictionary, count_array, word):
    #上から辞書を見ていって、アナグラムを見つけたら返す
    for i in range(len(dictionary)):
        flag = 1
        for j in range(len(count_array)):
            if dictionary[i][0][j]>count_array[j]:
                flag = 0
                break
        if flag:
            if(dictionary[i][1]!=word):
                return dictionary[i][1]
    return ""

if __name__=='__main__':
    dictionary = read_dictionary()
    text = read_textfile(sys.argv[1])

    ans_arr = []

    for i in range(len(text)):
        print(i)
        counting = count_word(text[i])
        ans = linear_search(dictionary, counting, text[i])
        print(ans)
        print()

        ans_arr.append(ans)

    #ファイル書き込み
    f = open(sys.argv[2], 'w')
    f.write('\n'.join(ans_arr))
    f.close()
