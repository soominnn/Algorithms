#include <iostream>

using namespace std;

int main()
{
    int i,j;
    string alphabet= "abcdefghijklmnopqrstuvwxyz";
    string s;
    cin >> s;
    for(i=0; i < 26; i++)
    {
        for(j=0; j < s.length(); j++)
        {
            if(s[j] == alphabet[i])
            {
                cout << j << ' ';
                break;
            }
        }
        if(s[j] != alphabet[i])
            cout << -1 << ' '; 
    }
}