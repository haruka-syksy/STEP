def read_dictionary():
    #ソートしてある辞書を読み込む
    f = open('new_dictionary.txt', 'r')
    data = f.read()
    f.close()

    list = data.split() #\nを除いて配列にする

    new = []
    for i in range(len(list)):#ソートした言葉と元の言葉をペアにする
        l = list[i].split(',')
        new.append((l[0], l[1]))
    return new

def binary_search(dictionary, value, word):
    #辞書を二分探索し、アナグラムのリストを返す
    ans = []
    def _binary_search(dictionary, value, left, right):
        if left > right:
            return ans #アナグラムがなかったら空文字列を返す

        mid = (left + right) // 2

        if dictionary[mid][0] == value:
            min_i = min_index(dictionary, mid)
            max_i = max_index(dictionary, mid)

            for i in range(min_i, max_i + 1):
                if dictionary[i][1] != word:
                    ans.append(dictionary[i][1])
            return ans

        elif dictionary[mid][0] < value:
            return _binary_search(dictionary, value, mid + 1, right)
        else:#numbers[mid] > value
            return _binary_search(dictionary, value, left, mid - 1)

    return _binary_search(dictionary, value, 0, len(dictionary)-1)

def min_index(dictionary, mid):
    min_i = -1
    if mid > 0:
        for i in range(mid-1, -1, -1):
            if dictionary[mid][0] != dictionary[i][0]:
                if min_i == -1:
                    min_i = mid
                return min_i
            else:
                min_i = i
                if i - 1 < 0:#アンダーフロー回避
                    return min_i
    else:
        return mid

def max_index(dictionary, mid):
    max_i = -1
    if mid < len(dictionary)-1:
        for i in range(mid+1, len(dictionary)):
            if dictionary[mid][0] != dictionary[i][0]:
                if max_i == -1:
                    max_i = mid
                return max_i
            else:
                max_i = i
                if(i + 1 >= len(dictionary)):#オーバーフロー回避
                    return max_i
    else:
        return mid


def word_sort(s):
    str = list(s)
    for i in range(len(str)):
        min_index = i
        for j in range(i+1, len(str)):
            if str[min_index] > str[j]:
                min_index = j
        str[min_index], str[i] = str[i], str[min_index]
    return ''.join(str)


if __name__=='__main__':
    new_dictionary = read_dictionary()

    print("何か英単語を入力してください！")
    word = input().strip()

    sorted_word = word_sort(word)

    ans = binary_search(new_dictionary, sorted_word, word)

    if ans == []:
        print("残念！アナグラムはなかったよ...")
    else:
        print(word+"のアナグラムはこちら！")
        for i in range(len(ans)):
            print(ans[i])
