front_index_list = [] #前カッコと後ろカッコの対応に使用

def read_number(line, index):
  number = 0
  while index < len(line) and line[index].isdigit():
    number = number * 10 + int(line[index])
    index += 1
  if index < len(line) and line[index] == '.':
    index += 1
    decimal = 0.1
    while index < len(line) and line[index].isdigit():
      number += int(line[index]) * decimal
      decimal /= 10
      index += 1
  token = {'type': 'NUMBER', 'number': number}
  return token, index


def read_plus(line, index):
  token = {'type': 'PLUS'}
  return token, index + 1

def read_minus(line, index):
  token = {'type': 'MINUS'}
  return token, index + 1

def read_multiply(line, index):
  token = {'type': 'MULTIPLY'}
  return token, index + 1

def read_divide(line, index):
  token = {'type': 'DIVIDE'}
  return token, index + 1

#前カッコの'index'と、後ろカッコの'front_index'で対応させる
def read_front_bracket(line, index):
  token = {'type': 'FRONTBRACKET', 'index': index}
  front_index_list.append(index)
  return token, index + 1

def read_back_bracket(line, index):
  front_index = front_index_list.pop()
  token = {'type': 'BACKBRACKET', 'front_index': front_index}
  return token, index + 1


def tokenize(line):
  tokens = []
  index = 0
  while index < len(line):
    if line[index].isdigit():
      (token, index) = read_number(line, index)
    elif line[index] == '+':
      (token, index) = read_plus(line, index)
    elif line[index] == '-':
      (token, index) = read_minus(line, index)
    elif line[index] == '*':
      (token, index) = read_multiply(line, index)
    elif line[index] == '/':
      (token, index) = read_divide(line, index)
    elif line[index] == '(':
      (token, index) = read_front_bracket(line, index)
    elif line[index] == ')':
      (token, index) = read_back_bracket(line, index)
    elif line[index] == 'q':
      print("finish!")
      exit(1)
    else:
      print('Invalid character found: ' + line[index])
      exit(1)
    tokens.append(token)
  return tokens


def evaluate_plus_minus(tokens):
    answer = 0
    index = 1
    while index < len(tokens):
      #足し算と引き算を計算
      if tokens[index]['type'] == 'NUMBER':
          if tokens[index - 1]['type'] == 'PLUS':
              answer += tokens[index]['number']
          elif tokens[index - 1]['type'] == 'MINUS':
              answer -= tokens[index]['number']
          else:

              print("plus")
              print(tokens)
              print("index")
              print(index)
              print('Invalid syntax')
              exit(1)
      index += 1
    return answer

def evaluate_multiply_divide(tokens, index):
    if tokens[index - 1]['type'] == 'MULTIPLY':#掛け算
        multi = tokens[index-2]['number']*tokens[index]['number']
        del tokens[index-2:index+1] #掛け算の式部分を削除
        index -= 2
        #掛け算の解を追加
        tokens.insert(index, {'type': 'NUMBER', 'number': multi})
    elif tokens[index - 1]['type'] == 'DIVIDE':#割り算
        if tokens[index]['number'] == 0:
            print("Can't divide by 0") #0では割れない
            return -1
        else:
            divi = tokens[index-2]['number']/tokens[index]['number']
        del tokens[index-2:index+1] #割り算の式部分を削除
        index -= 2
        #割り算の解を追加
        tokens.insert(index, {'type': 'NUMBER', 'number': divi})
    elif tokens[index - 1]['type'] == 'PLUS' or tokens[index - 1]['type'] == 'MINUS':
       #plus, minusなら何もしない
       index += 0
    else:
        print('Invalid syntax')
        exit(1)
    return index

def evaluate_brackets(tokens, index):
    #この前カッコに対応する後ろカッコの位置を探す
    for i in range(len(tokens)):
        if tokens[i]['type'] == 'BACKBRACKET':
            if tokens[index]['index'] == tokens[i]['front_index']:
                back_index = i
                break
    ans = evaluate(tokens[index+1:back_index]) #括弧の中身を計算
    #()内の式と括弧のtokensを消す
    del tokens[index:back_index+1]
    #()の計算の結果を追加
    tokens.insert(index, {'type': 'NUMBER', 'number': ans})


def evaluate(tokens):
  #answer = 0
  tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
  index = 1
  while index < len(tokens):
    if tokens[index]['type'] == 'NUMBER':
        #掛け算と割り算を計算
        index = evaluate_multiply_divide(tokens, index)
        if index == -1: #0で割るという式を与えられたとき-1が返ってくる
            return 0
        index += 1

    elif tokens[index]['type'] == 'FRONTBRACKET':
        #括弧内の計算
        evaluate_brackets(tokens, index)
    else:
        index += 1

  answer = evaluate_plus_minus(tokens) #足し算と引き算, 答えを返す
  return answer


def test(line):
  tokens = tokenize(line)
  actual_answer = evaluate(tokens)
  expected_answer = eval(line)
  if abs(actual_answer - expected_answer) < 1e-8:
    print("PASS! (%s = %f)" % (line, expected_answer))
  else:
    print("FAIL! (%s should be %f but was %f)" % (line, expected_answer, actual_answer))


# Add more tests to this function :)
def run_test():
  print("==== Test started! ====")
  #一桁
  test("0")
  test("1")
  test("1.0")
  test("-1")
  test("-1.0")
  #足し算
  test("1+2")
  test("1.0+2")
  test("1.0+1.2")
  test("-1.0+3")
  #引き算
  test("1-2")
  test("-3-1")
  test("1+(-3)")
  test("1.0-0.5")
  #掛け算
  test("2*2")
  test("0*1")
  test("-3*5")
  test("1.2*5")
  test("3.0*(-2)")
  test("1.5*2.0")
  #割り算
  test("4/2")
  test("-3/3")
  test("3/1.5")
  test("3.0/1.5")
  test("3.0/(-1.5)")
  #2演算
  test("1.0+2.1+3")#+->+
  test("1.0+2.1-3")#+->-
  test("1.0+2.1*3")#+->*
  test("1.0+2.1/3")#+->/

  test("1.0-2.1+3")#+->+
  test("1.0-2.1-3")#-->-
  test("1.0-2.1*3")#-->*
  test("1.0-2.1/3")#-->/

  test("1.0*2.1+3")#*->+
  test("1.0*2.1-3")#*->-
  test("1.0*2.1*3")#*->*
  test("1.0*2.1/3")#*->/

  test("1.0/2.1+3")#/->+
  test("1.0/2.1-3")#/->-
  test("1.0/2.1*3")#/->*
  test("1.0/2.1/3")#/->/

  #3演算以上
  test("3*1-2/2")
  test("3.0+4*2-1/5")
  #括弧
  test("-3*(3+4)")
  test("(3+4)*2")
  test("(3.0+4*(2-1))/5")
  test("(1+(1+2))/4")
  test("(1+(2+3)*5)/(7+6)")
  test("(1*(2+3)/10)")
  test("(1*(2+3)/10)+3+(2+1-(2*3)/4)")
  print("==== Test finished! ====\n")

run_test()

while True:
  print('> ', end="")
  line = input()
  tokens = tokenize(line)
  answer = evaluate(tokens)
  print("answer = %f\n" % answer)
