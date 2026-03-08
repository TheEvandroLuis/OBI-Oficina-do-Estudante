#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int main() {
    int n;
    int total=0;
    cin >> n;
    vector<int> chocolates;

    for (int i=0; i<n; i++){
        int c;
        cin>> c;
        chocolates.push_back(c);
    }
    sort(chocolates.rbegin(), chocolates.rend());

    for (int i=0; i<n; i++){
        //cout<<"Preço: "<< chocolates[i]<<endl;
        if ((i+1) % 3 != 0){
            total= total + chocolates[i];
            //cout<<"Total: "<< total<<endl;
        }
    }
    cout<<total<<endl;
}