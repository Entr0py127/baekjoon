#include <iostream>
#include <algorithm>
using namespace std;
int main(){
    int n,m;
    cin >> n;
    int card[n];
    for(int i=0;i<n;i++)
        cin >> card[i];
    cin >> m;
    int num[m];
    for(int i=0;i<m;i++)
        cin >> num[i];
    //입력

    sort(card,card+n);
    for(int i=0;i<m;i++){
        if(num[i]<=card[n-1] && num[i]>=card[0] && card[lower_bound(card,card+n,num[i])-card]==num[i])
            cout << 1 << ' ';
        else
            cout << 0 << ' ';
    }
}