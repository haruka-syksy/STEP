# Class6 Homework
malloc challenge!

## プログラム
- [first_fit.c](https://github.com/koomin-1122/STEP/blob/main/class6/first_fit.c) : First Fit(simple_malloc.cと同じ)
- [best_fit.c](https://github.com/koomin-1122/STEP/blob/main/class6/best_fit.c) : Best Fit
- [worst_fit.c](https://github.com/koomin-1122/STEP/blob/main/class6/worst_fit.c) : Worst Fit
- [right.c](https://github.com/koomin-1122/STEP/blob/main/class6/right.c) : freeする際に、**右側**につなげられる空き領域があれば領域を結合する
- [left.c](https://github.com/koomin-1122/STEP/blob/main/class6/left.c) : freeする際に、**左側**につなげられる空き領域があれば領域を結合する
- [bothsides.c](https://github.com/koomin-1122/STEP/blob/main/class6/bothsides.c) : freeする際に、**両側**につなげられる空き領域があれば領域を結合する
- [right_munmap.c](https://github.com/koomin-1122/STEP/blob/main/class6/right_munmap.c) : 右側につなげられる領域があれば結合し、munmapできる領域があればOSに返す
- [left_munmap.c](https://github.com/koomin-1122/STEP/blob/main/class6/left_munmap.c) : 左側につなげられる領域があれば結合し、munmapできる領域があればOSに返す
- [bothsides_munmap.c](https://github.com/koomin-1122/STEP/blob/main/class6/bothsides_munmap.c) : 両側につなげられる領域があれば結合し、munmapできる領域があればOSに返す
- [main.c](https://github.com/koomin-1122/STEP/blob/main/class6/main.c) 


## 実行
[Makefile](https://github.com/koomin-1122/STEP/blob/main/class6/Makefile)の2行目にある
```
SRCS=main.c first_fit.c simple_malloc.c
```
の`first.c`の部分を実行したいプログラム名に変える。<br>

ターミナルで
```
make run
```
と打つとsimple mallocとmy mallocのメモリ使用効率を比べることができる。
<br>


## メモリ使用率
|        | first fit | best fit | worst fit | right | left | bothsides | right<br>munmap | left<br>munmap | bothsides<br>munmap |
| -------| :-------: | :-------:| :-------: | :---: | :--: |  :-------: | :-------: | :-------: | :-------: |
| Challenge 1 |70%|70%|70%|70%|**71%**|**71%**|70%|**71%**|**71%**|
| Challenge 2 |40%|40%|40%|40%|40%|40%|40%|40%|40%|
| Challenge 3 |8%|**50%**|4% |48%| 46%|45%|48%|46%|45%|
| Challenge 4 |15%|71%|7% |**76%**|72%|75%|**76%**|72%|75%|
| Challenge 5 |15% |74%|7%|**77%**|76%|76%|**77%**|76%|76%|


## コメント
munmapで、いくつかのメモリは開放されているはずなのですが使用率が変わらなくて悲しいのでもう少し考えてみます！(malloc visualizerでOSに返せてそうなことが確認できました)<br>
あるmetadataのサイズが`4096 - sizeof(metadata_t)`より大きくても、領域の結合などの影響で`(uintptr_t)(metadata) % 4096`を満たすような位置にmetadataがないので、そこでまた分割できればもっと使用率が上がる気がします。<br><br>

malloc visualizerの上のグラフ、見るの楽しかったです！

