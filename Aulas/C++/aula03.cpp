#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<int> num = {1, 2 , 3, 4, 5};
    int a = 10;

    cout << a << endl;
    cout <<*&a << endl;
}