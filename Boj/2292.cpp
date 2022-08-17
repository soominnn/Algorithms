#include <iostream>

using namespace std;

int main()
{
    int i,n,cnt,tmp;
    cnt = 1;
    i = 1;
    cin >> n;
    if(n == 1)
        cout << 1;
    for(int i = 1; i<n; i++)
    {
        tmp = cnt;
        cnt += 6*i;
        cout << "tmp:" << tmp << "\n";
        cout << "cnt:" << cnt << "\n";
        cout << "i:" << i << "\n";
        if(n > tmp && n <= cnt)
        {
            cout << i+1; 
            break;
        }
    }
}