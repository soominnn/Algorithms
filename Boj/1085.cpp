#include <iostream>

using namespace std;

int main()
{
    int x,y,w,h;
    cin >> x >> y >> w >> h;
    if( w-x >= x && x <= y && x <= h-y)
        cout << x;
    else if(w-x < x && w-x < y && w-x < h-y)
        cout << w-x;
    else if(h-y >= y && y <= x && y <= w-x)
        cout << y;
    else if(h-y < y && h-y < x && h-y < w-x)
        cout << h-y;
}

