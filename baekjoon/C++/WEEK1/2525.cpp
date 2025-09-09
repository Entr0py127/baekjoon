#include <iostream>
using namespace std;
int main()
{
    int a,b,c;
    cin >> a >> b >> c;
    int h,m;
    h=c/60;
    m=c%60;
    b+=m,a+=h;
    if(b/60)
    {
        a+=b/60;
        b=b%60;
    }
    if(a/24)
        a%=24;
    cout << a << " " << b << endl;
}