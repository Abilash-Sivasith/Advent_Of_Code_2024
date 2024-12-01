#include <iostream>
#include <fstream>
#include <list>
#include <sstream>
#include <vector>
#include <cmath>
#include <map>
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
    ifstream textFile(textFileName);
    return textFile;
}

int main() {
    // auto advent_of_code_input = parseTextFile("aoc_day1.txt");
    auto advent_of_code_input = parseTextFile("aoc_day1.txt");
    if (!advent_of_code_input) {
        cerr << "Error: The file could not be openned";
        return 1;
    }

    vector<int> lhsList;
    map<int, int> rhsMap;
    string line;

    while (getline(advent_of_code_input, line)) {
        std::istringstream iss(line);
        int num1, num2;
        if (iss >> num1 >> num2) {
            lhsList.push_back(num1);
            // rhsList.push_back(num2);
            rhsMap[num2]++;
        }
    }
    int runningSum = 0;
    for (size_t i = 0; i < lhsList.size(); i++) {
        for (const auto &pair : rhsMap) {
            if (lhsList[i] == pair.first) {
                runningSum += (lhsList[i] * pair.second);
                break;
            }
        }
    }

    cout << "The runningSum is " << runningSum << "\n";


    /*
    // printing map
    for (auto it = rhsMap.begin(); it != rhsMap.end(); ++it) {
        cout << "Key: " << it->first << ", Value: " << it->second << endl;
    }
    */

    return 0;
}