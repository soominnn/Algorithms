#include <iostream>

using namespace std;

int main()
{
    string s;

    while(1)
    {
        cin >> s;
        if(s == "0")
            break;
        for(int i=0; i < s.length(); i++)
        {
            if(s[i] != s[s.length()-i-1])
            {
                cout << "no" << "\n";
                break;
            }
            if(i == s.length()-i-1 || i+1 == s.length()-i-1)
            {
                cout << "yes" << "\n";
            }
        } 
    }
}