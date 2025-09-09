#include <iostream>
#include <algorithm>
#include <string>
#include <utility>
#include <vector>
using namespace std;
bool compare(const tuple<int,string,int> &a,const tuple<int,string,int> &b)
{
    if(get<0>(a)==get<0>(b))
        return get<2>(a)<get<2>(b);
    return get<0>(a)<get<0>(b);
}

int main()
{
    int n;
    cin >> n;
    vector<tuple<int,string,int>> arr;
    for(int i=0;i<n;i++)
    {
        int a;
        string b;
        cin >> a >> b;
        arr.push_back({a,b,i});
    }
    sort(arr.begin(),arr.end(),compare);
    for(int i=0;i<n;i++)
    {
        cout << get<0>(arr[i]) << " " << get<1>(arr[i]) << "\n";
    }
}