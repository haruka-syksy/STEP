//Google渋谷間のみ
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <queue>
#include <list>
#include <algorithm>

void read_pages(std::map<std::string, std::string>& pages){
  //pages.txtを読み込む関数
  //std::map<std::string, std::string> pages;
  std::ifstream file("data/pages.txt");
  std::string data;
  while (std::getline(file, data)) {
    int index = data.find('\t');
    std::string id = data.substr(0, index);
    std::string title = data.substr(index + 1, data.size() - id.size() - 1);
    pages[id] = title;
    std::cout << "pages " << id << std::endl;
  }
}

void read_links(std::map<std::string, std::set<std::string> >& links){
  //links.txtを読み込む関数
  //std::map<std::string, std::set<std::string> > links;
  std::ifstream file("data/links.txt");
  std::string data;
  while (std::getline(file, data)) {
    int index = data.find('\t');
    std::string from = data.substr(0, index);
    std::string to = data.substr(index + 1, data.size() - from.size() - 1);
    links[from].insert(to);
    std::cout << "links " << from << std::endl;
  }
}

std::string find_page(std::map<std::string, std::string>& pages, std::string pagename){
  //ページの名前からkeyの値を取得する関数
  std::string page_key;
  for (const auto& page : pages) {
    if (page.second == pagename) {
      page_key = page.first;
      return page_key;
    }
  }
  //keyが見つからなければエラーを返して終了
  std::cout << "「" << pagename << "」のページはありませんでした！" << std::endl;
  exit(1);
}

std::list<std::string> bfs_make_path(
  std::string start_key,
  std::string target_key,
  std::map<std::string, std::string>& pages,
  std::map<std::string, std::set<std::string> >& links){
  //BFS(幅優先探索)を用いてスタートのページから目標のページまでのpathを作る関数
  std::queue<std::string> bfs; //bfs用のqueue
  std::set<std::string> checked; //探索済or探索予定のkeyを入れる
  std::map<std::string, std::list<std::string> > path; //start_keyから辿ったページの名前を保存

  bfs.push(start_key);

  while(!bfs.empty()){
    std::string search_key = bfs.front();
    checked.insert(search_key);//探索済に入れる
    bfs.pop();
    if(search_key == target_key){//見つかったらpathを返す
      return path[search_key];
    }
    else{
      for(auto itr = links[search_key].begin(); itr != links[search_key].end(); ++itr) {
        auto it = checked.find(*itr);//探索済or探索予定だったらqueueに入れない
        if(it != checked.end()){
          continue;
        }
        checked.insert(*itr);
        bfs.push(*itr);//queueに追加

        //pathを作る
        for(auto itr_p = path[search_key].begin(); itr_p != path[search_key].end(); ++itr_p){
          path[*itr].push_back(*itr_p);
        }
        path[*itr].push_back(pages[search_key]);
      }
    }
  }
  //見つからなければエラーを出して終了
  std::cout << "「" << pages[start_key] << "」と「" << pages[target_key] << "」のページは繋がっていないみたい..." << std::endl;;
  exit(1);
}

int main() {
  std::map<std::string, std::string> pages;
  std::map<std::string, std::set<std::string> > links;

  read_pages(pages);
  read_links(links);

  std::string start_key, target_key, search_key;
  std::string start_pagename = "Google", target_pagename = "六本木";

  start_key = find_page(pages, start_pagename);
  target_key = find_page(pages, target_pagename);

  std::list<std::string> path;
  path = bfs_make_path(start_key, target_key, pages, links);

  for(auto itr_p = path.begin(); itr_p != path.end(); ++itr_p){
    //pathを出力
    std::cout << *itr_p << " -> ";
  }
  std::cout << target_pagename << std::endl;

  return 0;
}
