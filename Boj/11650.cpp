#include <iostream>
#include <algorithm>
#include <utility>

using namespace std;

int main()
{
    int N, tmpx, tmpy;
    pair<int, int> arr[100000];
    cin >> N;
    for(int i=0; i<N; i++)
    {
        cin>>arr[i].first >> arr[i].second;
    }
    sort(arr, arr+N);
    for(int i=0; i<N; i++)
    {
        if(arr[i].first == arr[i+1].first && arr[i].second > arr[i+1].second)
        {
            tmpy = arr[i].first;
            arr[i].first = arr[i+1].first;
            arr[i+1].first = tmpy;
        }
    }
    for(int i=0; i<N; i++)
    {
        cout << arr[i].first << ' ' << arr[i].second << "\n";
    }
}