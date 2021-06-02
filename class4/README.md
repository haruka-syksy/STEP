# Week4 Homework
wikipediaのリンク構造を使って面白いことを見つける

## 使用言語
C++(g++ 4.2.1)

## プログラム
- [google_to_shibuya.cpp](https://github.com/koomin-1122/STEP/blob/main/class4/google_to_shibuya.cpp) : "Google"から"渋谷"までの経路を調べる
- (おまけ) [ken_search.cpp](https://github.com/koomin-1122/STEP/blob/main/class4/ken_search.cpp) : 47都道府県について、自分以外の県にリンクが接続しているか調べる。

## 実行
[wikipedia_data.zip](https://drive.google.com/file/d/1zqtjSb-ZoR4rzVUWZrjNSES5GKJhYmmH/view?usp=sharing) をダウンロードして解凍し、以下のようなディレクトリ構成にする。

```
step_wikipedia-graph
├── data
│   ├── graph_small.png
│   ├── links_small.txt
│   ├── links.txt
│   ├── pages_small.txt
│   └── pages.txt
├── README.md
├── google_to_shibuya.cpp
└── ken_search.cpp
```

### google_to_shibuya.cpp   
ターミナルで以下のコマンドを実行後、`./google_to_shibuya`を実行する。

```
g++ google_to_shibuya.cpp -o google_to_shibuya  
```
”Google”から”渋谷”までの経路が表示される。
`start_key`、`target_key`を変えれば他の経路も検索可能。


  
### ken_search.cpp 
(実行結果が長いので見るだけでも！google_to_shibuyaとプログラムはほぼ一緒です)      
ターミナルで以下のコマンドを実行後、`./ken_search`を実行する。
```
g++ ken_search.cpp -o ken_search -std=c++11
```

どちらもファイル(`pages.txt`, `links.txt`)の読み込みが、私の環境だと20分弱かかったので気長にお待ちください...(お時間取らせてしまいすみません)
    
## プログラムの説明
最短路検索ということで、幅優先探索を使用した。

### 関数ごとの説明
- **`read_pages`** : pages.txtを読み込み、ページのidをキー、titleを値としたmapを作成する。  
- **`read_links`** : links.txtを読み込み、ページのid(from)をキー、そのページでリンクされているページidたち(to)を値としたmapを作成する。  
- **`find_page`** : ページの名前からページのidを検索して返す。見つからなければエラーを返し終了。  
- **`bfs_make_path`** : 
  - queueを使って幅優先探索を行い、`start_key`から`target_key`までのパスを返す関数。queueにはページのidだけを入れている。
  - `start_key`から探索を行っていき、`target_key`と一致すれば、パスを返す。一致しなければ、そのページにリンクされているページのid(`links[search_key]`)をqueueに追加していく。  
  - すでに探索したid、探索予定のidは`checked`に入れ、無限ループが起こらないようにする。  
  - queueにidを追加する際、そのidまでのパスを更新する。(`search_key`の次のリンク先には、`search_key`の今までのパスと、`search_key`を入れる。)  
  - `target_key`が見つからなければエラーを出して終了。
  
### (おまけ)ken_search.cppの実行結果
面白いことを見つける、というのがなかなか思いつかなかったので、なんとなく47都道府県について、自分以外の県にリンクが接続しているか調べてみました。(例えば北海道なら、北海道以外の県(青森県〜沖縄県)にリンクが繋がっているか)
<br><br> [結果はこちら](https://docs.google.com/document/d/1zqsUkHi2acsurVZRwINStgRQ6r5azxt3JdnPVbne1CM/edit?usp=sharing)(Google Docsに飛びます)<br><br> 
結果、全ての県でそれぞれの県に1回のパスで繋がっている、すなわちある県のwikipediaの文章の中で、1回は全ての県のリンクが出てくることがわかりました。<br>
本当か？と思い今の埼玉県のwikipediaを調べてみたのですが、長崎県と鹿児島県のリンクがなかったので現在は違うかもしれないです...

### 追記 (2021/6/2)
Mutsuki Ikedaさんのコードを拝見して、mapを使っていたところをunordered_mapにしてみたところ、実行時間が10分くらいになりました！(約半分)
Mutsukiさん、ありがとうございます！！

#### Hikaruさんへ
mmapを使ってみたのですが、大きいファイルだとsegmentation faultになってしまったのでもう少し考えてみます！(smallの方ではうまくいってそうでした)








