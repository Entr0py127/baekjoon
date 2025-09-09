#include <iostream>
#include <algorithm>
using namespace std;
int main(){
    int n;
    cin >> n;
    int arr[n];
    int arr_1[n];
    for(int i=0;i<n;i++){
        cin >> arr[i];
        arr_1[i]=arr[i];
    }
    sort(arr_1,arr_1+n);
   /* for(int i=0;i<n;i++)
    cout << arr_1[i] << " ";
    cout << endl;*/
    int length=1;
    for (int i=0,j=1;j<n;) //i 자리에 넣고 비교는 j
        if(arr_1[i]!=arr_1[j])
            {arr_1[i+1]=arr_1[j];
            length++;
        i++;j++;}
        else
            while(arr_1[i]==arr_1[j])
                j++;

  /*for(int i=0;i<length;i++)
        cout << arr_1[i] << " ";
    cout << endl;*/
    int index;
    for(int i=0;i<n;i++){
        cout << lower_bound(arr_1,arr_1+length,arr[i])-arr_1 << " ";
    }
}