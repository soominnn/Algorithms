#include <iostream>

using namespace std;

int main()
{
    int i=0;
    int cnt=0;
    string s;
    getline(cin, s);
    while(s[i])
    {
        if(s[i] > 32 && s[i] <= 127 && (s[i+1] == ' ' || s[i+1] == '\0'))
        {
            cnt++;
        }        
        i++;
    }
    cout << cnt;
}