#include <iostream>
#include <string>
using namespace std;
int main()
{
    string s;
    float time;
    int time_total=0;
    float score_total=0;
    string score;

    for(int i=0;i<20;i++)
    {
        cin >> s >> time >> score;
        if(score!="P")
        {
            time_total+=time;
            if(score=="A+")
                score_total+=4.5*time;
            else if(score=="A0")
                score_total+=4.0*time;
            else if(score=="B+")
                score_total+=3.5*time;
            else if(score=="B0")
                score_total+=3.0*time;
            else if(score=="C+")
                score_total+=2.5*time;
            else if(score=="C0")
                score_total+=2.0*time;
            else if(score=="D+")
                score_total+=1.5*time;
            else if(score=="D0")
                score_total+=1.0*time;
        }
    }
    if(score_total==0)
        cout << 0;
    else
        cout << score_total/time_total;
}