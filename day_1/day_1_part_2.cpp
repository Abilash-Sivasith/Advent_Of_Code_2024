#include <iostream>
#include <fstream>
#include <list>
#include <sstream>
#include <vector>
#include <cmath>
using namespace std;

/*
Idea
    - similiar to part 1, but instead of storing the values in a vector use a 
      hashmap instead (similiar to python dicts)
    - go threw lhsList and multiple the lhsList[i] * rhsMap.at(lhsList[i]) and 
      ad to the running sum

to compile
    - g++ filename.gcc
    - ./a.out
*/


ifstream parseTextFile(string textFileName) {
    ifstream textFile("aoc_day1.txt");
    return textFile;
}

int main() {
    // auto advent_of_code_input = parseTextFile("aoc_day1.txt");
    auto advent_of_code_input = parseTextFile("testing1.txt");
    if (!advent_of_code_input) {
        cerr << "Error: The file could not be openned";
        return 1;
    }

    vector<int> lhsList;
    vector<int> rhsList; 
    string line;

    while (getline(advent_of_code_input, line)) {
        std::istringstream iss(line);
        int num1, num2;
        if (iss >> num1 >> num2) {
            lhsList.push_back(num1);
            rhsList.push_back(num2);
        }
    }
    sort(rhsList.begin(), rhsList.end());
    sort(lhsList.begin(), lhsList.end());


    return 0;
}