#include <iostream>
#include <algorithm>
#include <utility>

using namespace std;

bool cmp(pair<int,string> a, pair<int,string> b)
{
    return a.first < b.first;
}

int main()
{
    int N;
    string tmp;
    cin >> N;
    pair<int,string> arr[100000];
    for(int i=0; i<N; i++)
    {
        cin>>arr[i].first >> arr[i].second;
    }
    stable_sort(arr, arr + N,cmp);
    
    for(int i=0; i<N; i++)
    {
        cout << arr[i].first << ' ' << arr[i].second << "\n";
    }
}

