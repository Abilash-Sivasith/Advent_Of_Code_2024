/*
Idea:
    put LHS numbers into list1
    put RHS numbers into list2
    sort list1 and list2
    go through the list a keep a count of the abs(list1[i] - list2[i])
*/

#include <iostream>
#include <fstream>
using namespace std;
#include <list>
#include <sstream>
#include <vector>
#include <cmath>

ifstream parseTextFile(string textFileName) {
    ifstream textFile(textFileName);
    return textFile;
}

int main() {
    auto advent_of_code_input = parseTextFile("aoc_day1.txt");
    if (!advent_of_code_input) {
        cerr << "Error: The file could not be openned";
        return 1;
    }

    vector<int> lhsList;
    vector<int> rhsList; // using vectors because they are dynamically allocated
    string line;

    while (getline(advent_of_code_input, line)) {
        std::istringstream iss(line);
        int num1, num2;
        if (iss >> num1 >> num2) {
            lhsList.push_back(num1);
            rhsList.push_back(num2);
        }
    }

    // sort lhsList and rhsList
    sort(rhsList.begin(), rhsList.end());
    sort(lhsList.begin(), lhsList.end());

    // cout << "lhslist size -> " << lhsList.size() << "\n";
    // cout << "lhslist size -> " << rhsList.size() << "\n";

    int runningSum = 0;
    // find the abs() difference
    for (int i = 0; i < lhsList.size(); i++) {
        // cout << lhsList[i] - rhsList[i];
        runningSum += std::abs(lhsList[i] - rhsList[i]);
        // cout << runningSum << "\n";
    }

    // printing lhsList out
    /*
    for (int i = 0; i < lhsList.size(); i++) {
        cout << lhsList[i] << "\n";
        cout << rhsList[i] << "\n";
    }
    */
    

    advent_of_code_input.close();
    
   cout << "The total sum is --> " << runningSum << "\n";
    return 0;
}
