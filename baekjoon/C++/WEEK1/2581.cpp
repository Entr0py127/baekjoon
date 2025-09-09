#include <iostream>
#include <vector>
#include <cmath>
using namespace std;
vector <int> prime;
bool isprime(int n)
{
    for(int i=0;prime[i]<=sqrt(n);i++)
    {
        if(n%prime[i]==0)
            {
                return false;
            }
    }
    return true;
}
int main()
{
    int m,n;
    cin >> m >> n;
    int sum=0;
    int min=10000;
    prime.push_back(2);
    if(m<=2&&n>=2)
        {sum+=2;
        min=2;}
    for(int i=3;i<=n;i+=2)
    {
        if(isprime(i))
        {
            prime.push_back(i);
            if(i>=m)
            {
                sum+=i;
                if(min>i)
                    min=i;
            }
        }
    }
    if(min==10000)
        cout << -1 << endl;
    else
        {
            cout << sum << endl;
            cout << min << endl;
        }
}
