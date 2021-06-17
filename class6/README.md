# Class6 Homework
malloc challenge!

## プログラム
- [first_fit.c] : First Fit(simple_malloc.cと同じ)
- [best_fit.c](https://github.com/koomin-1122/STEP/blob/main/class5/greedy_2opt.py) : Best Fit
- [worst_fit.c](https://github.com/koomin-1122/STEP/blob/main/class5/greedy_2opt_center.py) : Worst Fit
- [right.c](https://github.com/koomin-1122/STEP/blob/main/class5/greedy_2opt_start.py) : freeする際に、**右側**につなげられる空き領域があれば領域を結合する
- [left.c](https://github.com/koomin-1122/STEP/blob/main/class5/greedy_2opt_start.py) : freeする際に、**左側**につなげられる空き領域があれば領域を結合する
- [bothsides.c](https://github.com/koomin-1122/STEP/blob/main/class5/greedy_2opt_start.py) : freeする際に、**両側**につなげられる空き領域があれば領域を結合する
- [right_munmap.c](https://github.com/koomin-1122/STEP/blob/main/class5/greedy_2opt_start.py) : 右側につなげられる領域があれば結合し、munmapできる領域があればOSに返す
- [left_munmap.c](https://github.com/koomin-1122/STEP/blob/main/class5/greedy_2opt_start.py) : 左側につなげられる領域があれば結合し、munmapできる領域があればOSに返す
- [bothsides_munmap.c](https://github.com/koomin-1122/STEP/blob/main/class5/greedy_2opt_start.py) : 両側につなげられる領域があれば結合し、munmapできる領域があればOSに返す

## 実行

## プログラムの説明

## スコア
|        |greedy+2-opt <br>start with a good point|greedy+2-opt<br>start with a center point| greedy+2-opt | greedy | Simulated Annealing | 
| ---------------     | :-------------------------------------------: | :-------------------------------------------:| :-----------------: | :----: | :-----------------: | 
| input_0.csv (n=5)   |3291.62|3418.10|3418.10              |3418.10 |3291.62              | 
| input_1.csv (n=8)   |3778.72|4019.57|3832.29              |3832.29 |3778.72              | 
| input_2.csv (n=16)  |4494.42|4670.27|4994.89              |5449.44 |4494.42              | 
| input_3.csv (n=64)  |8424.72|8736.94|8970.05              |10519.16|8150.91              | 
| input_4.csv (n=128) |10839.97|11216.04|11489.79             |12684.06|10675.29             | 
| input_5.csv (n=512) |20950.18|21536.66| 21376.27            |25331.84|21119.55             | 
| input_6.csv (n=2048)|41855.51|42596.79| 42712.37            |49892.05|44393.89             | 
<br>

## コメント
