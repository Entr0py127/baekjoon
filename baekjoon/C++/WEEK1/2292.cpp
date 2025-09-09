#include <iostream>
#include <vector>
using namespace std;
int main()
{
    int n;
    cin >> n;
    vector <int> arr;
    arr.push_back(1);
    for(int i=1;arr.back()<n;i++)
    {
        arr.push_back(arr.back()+6*i);
    }
    cout << arr.size();
}