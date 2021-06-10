# Week5 Homework
巡回セールスマン問題(TCP)に挑戦！

## プログラム
### https://github.com/hayatoito/google-step-tsp からダウンロードしたもの
- [common.py](https://github.com/koomin-1122/STEP/blob/main/class5/common.py) : データの読み込みと出力を行う関数が入っている(greedy_2opt.py, greedy_2opt_center.py, greedy_2opt_start.pyで使われている)
- [output_verifier.py](https://github.com/koomin-1122/STEP/blob/main/class5/output_verifier.py) : スコアを出力する

### 自分で作ったor変更したもの
- [greedy_2opt.py](https://github.com/koomin-1122/STEP/blob/main/class5/greedy_2opt.py) : greedyのアルゴリズムと2-opt法を組み合わせたプログラム
- [greedy_2opt_center.py](https://github.com/koomin-1122/STEP/blob/main/class5/greedy_2opt_center.py) : greedy_2opt.pyで、真ん中らへんの点からスタートする
- [greedy_2opt_start.py](https://github.com/koomin-1122/STEP/blob/main/class5/greedy_2opt_start.py) : greedy_2opt.pyで、一番経路が短くなるスタートの点を探して、その経路を返す
- [output.py](https://github.com/koomin-1122/STEP/blob/main/class5/output.py) : 受け取ったプログラムを使って、input_0.csv ~ input06.csvを入力データとして読み込みoutput_0.csv~output_6.csvに出力する


## 実行
#### greedy_2opt.py<br>greedy_2opt_center.py<br>greedy_2opt_start.py

```
python greedy_2opt.py [入力ファイル(input_0.csv ~ input_6.csv)]
```
できた経路が標準出力に表示される
(greedy_2opt_start.pyだけinput_6.csvに5時間くらいかかりました)

#### output.py

```
python output.py [実行したいプログラム(greedy_2opt.py, greedy_2opt_center.py, greedy_2opt_start.py)]
```
できた経路がカレントディレクトリにoutput_０.csv ~ output_6.csvとして保存される<br>


#### output_verifier.py
```
python output.py [実行したいプログラム(greedy_2opt.py, greedy_2opt_center.py, greedy_2opt_start.py)]
```
自分の経路と、randomと、greedyと、saのスコアが表示される

## プログラムの説明
greedyのアルゴリズムと、2-opt法のようなものを組み合わせた。<br>
greedyのアルゴリズムは、 https://github.com/hayatoito/google-step-tsp からダウンロードしたsolver_greedy.pyの関数をそのまま使用した。<br>
- `two_opt関数`では、辺同士が交差しているかどうかに関わらず今つながっている辺よりも短いものがあれば繋ぎ変えている。交差は解消していたので2-opt法のようなものだと思っている...。
<br><br>
## スコア
|                     |greedy+2-opt <br>start with a good point|greedy+2-opt<br>start with a center point| greedy+2-opt | greedy | Simulated Annealing | 
| ---------------     | :-------------------------------------------: | :-------------------------------------------:| :-----------------: | :----: | :-----------------: | 
| input_0.csv (n=5)   |3291.62|3418.10|3418.10              |3418.10 |3291.62              | 
| input_1.csv (n=8)   |3778.72|4019.57|3832.29              |3832.29 |3778.72              | 
| input_2.csv (n=16)  |4494.42|4670.27|4994.89              |5449.44 |4494.42              | 
| input_3.csv (n=64)  |8424.72|8736.94|8970.05              |10519.16|8150.91              | 
| input_4.csv (n=128) |10839.97|11216.04|11489.79             |12684.06|10675.29             | 
| input_5.csv (n=512) |20950.18|21536.66| 21376.27            |25331.84|21119.55             | 
| input_6.csv (n=2048)|41855.51|42596.79| 42712.37            |49892.05|44393.89             | 

## コメント
`greedy_2opt_center.py`では、中心からスタートした方が、最終点から最初の点まで戻ってくるときの距離が長くなりにくいのではないか(端から端まで線を引くようなことにはならない)、という考えを基に、真ん中の点を探してそこからパスを作った。0の点からスタートする`greedy_2opt.py`と比較すると、n=16より多いデータで少しスコアの改善が見られた。<br>
スタートの点がスコアに関係してくることがわかったので、`greedy_2opt_start.py`では全ての点をスタート点としてその経路を比べ、一番短いものを出力するようにした。すると、全ての入力データでスコアに改善が見られた。
