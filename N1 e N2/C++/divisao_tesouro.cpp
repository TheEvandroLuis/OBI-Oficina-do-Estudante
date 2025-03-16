#include <iostream>
using namespace std;

int main() {
    int a, n, quota;

    cin >> a;
    cin >> n;

    n = n+2; 
    quota = a/n;

    cout << quota*2;
}