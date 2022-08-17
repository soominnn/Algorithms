#include <iostream>

using namespace std;

int main()
{
    int a;
    int b;
    int ch1;
    int ch2;
    cin >> a;
    cin >> b;

    ch1 = (a%10)*100 + ((a%100)-(a%10)) + (a/100);
    ch2 = (b%10)*100 + ((b%100)-(b%10)) + (b/100);

    if (ch1>ch2)
        cout << ch1;
    else 
        cout << ch2;
}