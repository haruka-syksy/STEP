# Week4 Homework
wikipediaのリンク構造を使って面白いことを見つける

## 使用言語
C++(g++ 4.2.1)

## プログラム
- google_to_shibuya.cpp : "Google"から"渋谷"までの経路を調べる
- 

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
└── google_to_shibuya.cpp
```

ターミナルで以下のコマンドを実行後、`./google_to_shibuya`を実行する。

```
g++ google_to_shibuya.cpp -o google_to_shibuya  
```
”Google”から”渋谷”までの経路が表示される。

ファイル(`pages.txt`, `links.txt`)の読み込みに20分弱かかるので気長にお待ちください...

## プログラムの説明
最短路検索ということで、幅優先探索を使用した。

### 関数ごとの説明
- **`read_pages`** : pages.txtを読み込み、ページのidをキー、titleを値としたmapを作成する。
- **`read_links`** : links.txtを読み込み、ページのid(from)をキー、そのページでリンクされているページidたち(to)を値としたmapを作成する。
- **`find_page`** : ページの名前からページのidを検索して返す。見つからなければエラーを返し終了。
- **`bfs_make_path`** : queueを使って幅優先探索を行い、`start_key`から`target_key`までのパスを返す関数。queueにはページのidだけを入れている。
`start_key`から探索を行っていき、`target_key`と一致すれば、パスを返す。一致しなければ、そのページにリンクされているページのid(`links[search_key]`)をqueueに追加していく。  
すでに探索したid、探索予定のidは`checked`に入れ、無限ループが起こらないようにする。  
queueにidを追加する際、そのidまでのパスを更新する。(`search_key`の次のリンク先には、`search_key`の今までのパスと、`search_key`を入れる。)
`target_key`が見つからなければエラーを出して終了。
