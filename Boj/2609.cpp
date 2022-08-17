#include <iostream>
#include <string>

using namespace std;

int main()
{
    int n1,n2,cnt,tmp1,tmp2,max;
    cnt = 1;
    cin >> n1 >> n2;
    while(1)
    {
        if(cnt > n1 || cnt > n2)
            break;
        if(n1 % cnt == 0)
            tmp1 = cnt;
        if(n2 % cnt == 0)
            tmp2 = cnt;
        if(tmp1 == tmp2)
            max = tmp1;
        cnt++;
    }
    cout << max << "\n";
    cout << max*(n1/max)*(n2/max); 
}