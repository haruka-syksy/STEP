# Week7 Homework
帰ってきた！！巡回セールスマン問題(TCP)

## プログラム
### https://github.com/hayatoito/google-step-tsp からダウンロードしたもの
- [output_verifier.py](https://github.com/koomin-1122/STEP/blob/main/class5/output_verifier.py) : スコアを出力する

### 自分で作ったもの
- [divide.py](https://github.com/koomin-1122/STEP/blob/main/class7/divide.py) 

下の図のように4つに領域分割して、分割したそれぞれの領域でgreedy法と2-opt法を用いて短い経路を見つける。<br><br>


![領域分割](https://user-images.githubusercontent.com/70313656/123937216-e7c7fb80-d9d0-11eb-9672-b4f0a3ab1277.png)

最後に領域ごとの経路を結合する。
結合の際に経路がどうしても交差してしまったため、全体の経路に関して2-opt法を行なっている。<br><br><br>



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

##実行結果
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
https://koomin-1122.github.io/STEP/class5/visualizer/build/default/

###実行時間
class5での自分のスコアを超えることはできなかったのですが、領域分割をしたことで実行時間がかなりはやくなりました！<br>
####divide.pyの実行時間
class5での自分のスコアを超えることはできなかったのですが、領域分割をしたことで実行時間がかなりはやくなりました！<br>

input 0  time: 0.001853 sec<br>
input 1  time: 0.000682 sec<br>
input 2  time: 0.000961 sec<br>
input 3  time: 0.013946 sec<br>
input 4  time: 0.047842 sec<br>
input 5  time: 1.250135 sec<br>
input 6  time: 17.461804 sec<br>
input 7  time: 445.561465 sec<br>

greedy_2opt_start.py


## コメント
