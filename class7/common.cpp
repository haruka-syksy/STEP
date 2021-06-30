#include <iostream>
#include <fstream>
#include <vector>
#include <stdlib.h>


std::vector<std::pair<long double, long double> > read_input(std::string filename){
  std::vector<std::pair<long double, long double> > cities;
  std::ifstream file(filename);
  std::string data;
  std::getline(file, data);//1行目無視
  while (std::getline(file, data)) {
    int index = data.find(',');
    std::string x = data.substr(0, index);
    std::string y = data.substr(index + 1, data.size() - x.size() - 1);
    //std::cout << x << " " << y << std::endl;

    //ここの変換のところで桁落ちしている？
    cities.push_back(std::make_pair((long double)std::stod(x), (long double)std::stod(y)));
    //cities.push_back(std::make_pair(std::stod(x), std::stod(y)));
  }
  return cities;
}

void write_output(std::vector<int> tour){
  std::ofstream outputfile("test.txt");
    outputfile<<"index" << std::endl;
    for(int i=0;i<tour.size();i++){
      outputfile<< std::to_string(tour[i]) << std::endl;
    }
    outputfile.close();
}

/*
int main(){
  std::vector<std::pair<long double, long double> > cities;
  cities = read_input("input_0.csv");

  for(int i=0;i<cities.size();i++){
    std::cout << cities[i].first << " " << cities[i].second << std::endl;
  }
}

*/
