// Example program
#include <iostream>
using namespace std;

int main(){
    int a, b, c, d, diff;
    cin>>a;
    cin>>b;
    cin>>c;
    cin>>d;

    if (d+a > b+c){
        cout<<d+a - b+c;
    }else{
        cout<<b+c - d+a;
    }

    return 0;
}