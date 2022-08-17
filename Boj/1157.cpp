#include <iostream>

using namespace std;

int main()
{
    string s;
    cin >> s;
    int count[26]={0, };
    for(int i=0; i< s.length(); i++)
    {
        
        if(s[i]<97)
            s[i] -= 65;
        else
            s[i] -= 97;
        count[s[i]]++;
    }

    int max=0;
    int max_index;
    bool overlap=false;
    for(int i=0; i<26; i++)
    {
        if(count[i] > max)
        {
            max = count[i];
            max_index = i;
            overlap = false;
        }
        else if(max == count[i])
            overlap = true;
    }
    if(overlap)
        cout<< '?';
    else 
        cout << char(max_index + 65);
}