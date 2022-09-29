//MYID
#include <bits/stdc++.h>
#include <stdio.h>
#include <vector>

#define pb push_back
using namespace std;
vector<vector<string>> a;
    bool ok = 0;

void Setup() {

    FILE *fp;

    fp = freopen("/etc/passwd", "r", stdin);
    string s;
    while(getline(cin, s)) {
//        cout << s << '\n';
//        fprintf(fp, "%s", s);
        string t;
        string cur;
        vector<string> tmp;
        for(char c : s) {
            if(c == ':') {
                tmp.pb(cur);
                cur = "";
            } else {
                cur += c;
            }
        }
        a.pb(tmp);
    }
   fclose(fp);
//    fclose(temp);
}

void Check(vector<string> v, string a) {
    if(v.size() && v[0] == a) {
        cout << "Username                      : " << a << '\n';
        cout << "Encrypted password            : " << v[1] << '\n';
        cout << "User ID number (UID)          : " << v[2] << '\n';
        cout << "User's group ID number (GID)  : " << v[3] << '\n';
        cout << "Full name of the user (GECOS) : " << v[4] << '\n';
        cout << "User home directory           : " << v[5] << '\n';
        ok = 1;
    }
}
int main(int argc, char** argv){
    if (argc > 1 && std::string(argv[1]) == "-xterm") {
        if (::execl("/usr/bin/xterm", "xterm", "-e", argv[0], (char*)NULL)) {
      std::perror("execl");
      return 1;
        }
    }

//    freopen("output.txt", "w", stdout);

    cout << "Nhap ten username: ";
    string un;
    cin >> un;
    Setup();
//    cout << un << '\n';
    for(int i = 0; i < a.size(); ++i) {
        Check(a[i], un);
    }
    if(!ok) {
        cout << "Khong tim thay username tuong ung.\n";
    }
    return 0;
}
