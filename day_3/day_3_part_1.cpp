
#include <iostream>
#include <fstream>
#include <regex>
#include <string>
#include <cctype>
using namespace std;

/*
Big thanks for the help,
https://www.geeksforgeeks.org/regex-regular-expression-in-c/
*/


ifstream parseFile(string textFileName) {
    ifstream TextFile(textFileName);
    return TextFile;
}

bool isValidInteger(const string& s) {
    return !s.empty() && all_of(s.begin(), s.end(), ::isdigit);
}

int main() {
    auto FileInput = parseFile("testing.txt");
    if (!FileInput) {
        cerr << "Error: Could not open the file";
    }
    string Line;
    while (getline(FileInput, Line)) 
    {
        regex r("mul\\([0-9]+,[0-9]+\\)"); 
        smatch m;
        auto WordsBegin = sregex_iterator(Line.begin(), Line.end(), r);
        auto WordsEnd = sregex_iterator(); 

        for (sregex_iterator i = WordsBegin; i != WordsEnd ; ++i) 
        {
            cout << "Found: " << i->str() << " ";
            string num1_str = (*i)[1];
            string num2_str = (*i)[2];
            int num1  = stoi(num1_str);
            if (isValidInteger(num1_str) && isValidInteger(num2_str)) 
            {
                int num1 = stoi(num1_str);
                int num2 = stoi(num2_str);
                cout << num1 + num2;
            }
        }

    }
    FileInput.close();
    return 0;
}