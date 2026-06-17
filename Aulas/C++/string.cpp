#include <iostream>
#include <string>
using namespace std;

int main(){
    char str1;
    cin >> str1;
    int n = int(str1) - 65;
    n = n +4;
    cout << char(n+65) << endl;

    return 0;
}
