#include <iostream>
#include <algorithm>
#include <utility>
using namespace std;
bool compare(pair<int,int> a, pair<int,int> b){
    if(a.second==b.second)
        return a.first<b.first;
    return a.second<b.second;
}
int main(){
    int n;
    cin >> n;
    pair <int,int> arr[n];
    for (int i=0;i<n;i++){
        cin >> arr[i].first >> arr[i].second;
    }
    sort(arr,arr+n,compare);
    for (int i=0;i<n;i++){
        cout << arr[i].first << ' ' << arr[i].second << '\n';
    }
}