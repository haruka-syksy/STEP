def word_sort(s):
    #単語をアルファベット順にソートする
    str = list(s)
    for i in range(len(str)):
        min_index = i
        for j in range(i+1, len(str)):
            if str[min_index] > str[j]:
                min_index = j
        str[min_index], str[i] = str[i], str[min_index]
    return ''.join(str)

def new_dictionary_sort(dictionary):
    #アルファベット順にした単語をソートする
    for i in range(len(dictionary)):
        min_index = i
        for j in range(i, len(dictionary)):
            if dictionary[min_index][0] > dictionary[j][0]:
                min_index = j
        dictionary[min_index], dictionary[i] = dictionary[i], dictionary[min_index]
    return dictionary

def make_new_dictionary(dictionary):
    #(ソートした単語, 元の単語)のペアを作って新しい辞書を作る
    new = []
    for i in range(len(dictionary)):
        new.append(((word_sort(dictionary[i])), dictionary[i]))
    new_sorted = new_dictionary_sort(new)

    return new_sorted

if __name__=='__main__':
    f1 = open('words.txt', 'r')
    data = f1.read()
    f1.close()
    dictionary = data.split() #\nを除いて配列にする

    new_dictionary = []
    new_dictionary = make_new_dictionary(dictionary)

    f2 = open('new_dictionary.txt', 'w')
    for word in new_dictionary:
        print(*word, sep=',', file=f2)
    f2.close()
