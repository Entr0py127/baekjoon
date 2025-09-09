#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
int main()
{
    int n,m;
    cin >> n >> m;
    string s[n];
    string arr[m];
    for (int i=0;i<n;i++)
        cin >> s[i];  
    for (int i=0;i<m;i++)
        cin >> arr[i];
    sort(s,s+n);
   int cnt=0;
    for(int i=0;i<m;i++){
        if(binary_search(s,s+n,arr[i]))
            cnt++;
    }
    cout << cnt;
}