#include <iostream>
using namespace std;
int main()
{
    int n=9;
    int arr[9][9];
    int max=-1;
    int x,y;
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            cin >> arr[i][j];
            if(arr[i][j]>max)
            {
                max=arr[i][j];
                x=i+1;
                y=j+1;
            }
        }
    }
    cout << max << endl;
    cout << x << " " << y << endl;
}