#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int a, b;
    vector<int> c;
    int m =0;
    cin >> a;
    cin >> b;

    //SENDO A MEDIA E MEDIANA = A
    m = (2*a) - b;
    c.push_back(m);

    //SENDO A MEDIA E MEDIANA = B
    m = (2*b) - a;
    c.push_back(m);

    //SENDO A MEDIA E MEDIANA IGUAL C
    m = int((a+b)/2);
    c.push_back(m);

    sort(c.begin(), c.end());
    cout<<c[0]<<endl;
}