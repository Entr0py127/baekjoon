#include <iostream>
#include <string>
using namespace std;
int main()
{
    string s;
    cin >> s;
    int alphabet[26]={};
    for(int i=0;i<s.length();i++)
    {
        if(s[i]>='a' && s[i]<='z')
            alphabet[s[i]-'a']++;
        else
        alphabet[s[i]-'A']++;
    }
    int max=-1,index;
    for(int i=0;i<26;i++)
    {
        if(alphabet[i]>max)
        {
            max=alphabet[i];
            index=i;
        }
        else if(alphabet[i]==max)
            index=-1;
    }
    if(index==-1)
        cout << "?" << endl;
    else
        cout << (char)(index+'A') << endl;
}