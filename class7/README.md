# Week7 Homework

# 宿題1, 宿題2
- [matrix.c](https://github.com/koomin-1122/STEP/blob/main/class7/matrix/matrix.c) 
- [matrix.py](https://github.com/koomin-1122/STEP/blob/main/class7/matrix/matrix.py) <br>

### 考察
[google docに飛びます](https://docs.google.com/document/d/1UiecD7neJazwShi5jB8mpxBnIw0S8OEhczzVMle1nuk/edit?usp=sharing)

<br>

# 宿題3
帰ってきた！！巡回セールスマン問題(TCP)

## プログラム
### https://github.com/hayatoito/google-step-tsp からダウンロードしたもの
- [output_verifier.py](https://github.com/koomin-1122/STEP/blob/main/class5/output_verifier.py) : スコアを出力する

### 自分で作ったもの
- [divide.py](https://github.com/koomin-1122/STEP/blob/main/class7/divide.py) 

下の図のように4つに領域分割して、分割したそれぞれの領域でgreedy法と2-opt法を用いて短い経路を見つける。<br><br>


![領域分割](https://user-images.githubusercontent.com/70313656/123937216-e7c7fb80-d9d0-11eb-9672-b4f0a3ab1277.png)

最後に領域ごとの経路を結合する。
結合の際に経路がどうしても交差してしまったため、全体の経路に関して再度2-opt法を行った。<br><br>



## 実行
#### divide.py

```
python divide.py
```
input_0.csv ~ input_7.csvを読み込み、できた経路がカレントディレクトリにoutput_０.csv ~ output_7.csvとして保存される<br>


#### output_verifier.py
```
python output_verifier.py 
```
自分の経路と、randomと、greedyと、saのスコアが表示される

<br><br>

## 実行結果
### スコア
|                     | divide.py | class5でのベストスコア<br>(greedy_2opt_start.py)|greedy | Simulated<br>Annealing | 
| ---------------     | :-----------------: | :----: | :----: | :-----------------: | 
| input_0.csv (n=5)   |3418.10|3291.62|3418.10 |3291.62              | 
| input_1.csv (n=8)   |4061.62|3778.72|3832.29 |3778.72              | 
| input_2.csv (n=16)  | 4494.42|4494.42|5449.44 |4494.42              | 
| input_3.csv (n=64)  |9117.82|8424.72|10519.16|8150.91              | 
| input_4.csv (n=128) |11653.97|10839.97|12684.06|10675.29             | 
| input_5.csv (n=512) |21727.67|20950.18|25331.84|21119.55             | 
| input_6.csv (n=2048)|43257.98|41855.51|49892.05|44393.89             | 
| input_7.csv (n=8192) |85318.87|実行中...|95983.29|?|
<br>
divide.pyの経路はこちらで見ることができます！<br>

https://koomin-1122.github.io/STEP/class7/visualizer/build/default/

<br>

### 実行時間
class5での自分のスコアを超えることはできなかったのですが、領域分割をしたことで実行時間がかなりはやくなりました！<br>
#### divide.pyの実行時間
||sec|
| --------- | :-----------: |
| input_0.csv (n=5)   |0.001853 | 
| input_1.csv (n=8)   |0.000682| 
| input_2.csv (n=16)  |0.000961| 
| input_3.csv (n=64)  |0.013946| 
| input_4.csv (n=128) |0.047842|
| input_5.csv (n=512) |1.250135|
| input_6.csv (n=2048)|17.461804|
| input_7.csv (n=8192)|445.561465| 

<br>

#### greedy_2opt_start.py(class5のプログラム)の実行時間
input6に3時間くらいかかってました！<br>
実行が終わらないのでまた追記します...

<br>

## コメント
領域の分割の仕方(今は単純に4分割)や、領域ごとの経路の結合の仕方を工夫したらもっと良い経路が見つかると思うので、思いついたらまた実装したいです!

<br>

## 質問
C++で実装しようと試みたのですが、データを読み込むところで桁落ちが起こってしまいました。([common.cpp](https://github.com/koomin-1122/STEP/blob/main/class7/common.cpp#L18-L19))<br>

`214.98279057984195 -> 214.983`<br>
`762.6903632435094  -> 762.69`

上のような感じです。string型からdouble型の変換で調べてみたのですが、よくわからなかったので桁落ちせずに変換できる方法があれば教えていただきたいです。


