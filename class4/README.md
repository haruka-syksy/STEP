## 使用言語
C++(g++ 4.2.1)

## プログラム
- google_to_shibuya.cpp : "Google"から"渋谷"までの経路を調べる

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
