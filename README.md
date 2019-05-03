# back-to-98

## Philosophy
Make your C++ code better than ever.

## Features
* Replace `nullptr` with `NULL`
* Replace unstable `map` with time-tested `set<pair<T, K> >`
* Replace unreadable `>>` with `> >`
* TODO: ...

## Usage
```zsh
➜  20to98 git:(master) ✗ cat cp.cpp
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    cin >> n;

    map<long long, map<string, vector<long long> >> m;

    return 0;
}
➜  20to98 git:(master) ✗ python3 backto98.py cp.cpp
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long n;
    cin >>  n;

    set<pair<long long, set<pair<string, vector<long long> > > > >  m;

    return 0;
}

Done.
```