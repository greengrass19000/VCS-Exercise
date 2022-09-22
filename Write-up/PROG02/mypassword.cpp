#include <bits/stdc++.h>
#include <crypt.h>
#include <unistd.h>
#include <time.h>
#define pb push_back
using namespace std;
std::string execute_command(std::string cmd) {
    std::array<char, 128> buffer;
    std::string result;
    
    #if defined(_WIN32)
        #define POPEN _popen
        #define PCLOSE _pclose
    #elif defined(unix) || defined(__unix__) || defined(__unix)
        #define POPEN popen
        #define PCLOSE pclose
    #endif

    std::unique_ptr<FILE, decltype(&PCLOSE)> pipe(POPEN(cmd.c_str(), "r"), PCLOSE);
    if (!pipe) 
    {
        throw std::runtime_error("popen() failed!");
    }
    while (fgets(buffer.data(), buffer.size(), pipe.get()) != nullptr) 
    {
        result += buffer.data();
    }
    return result;
}

string un, ep, p, nep, thes, thenews;
std::vector<string> v;

string takeEP(string s) {
    int run = 0;
    while(s[run] != ':') ++run;
    ++run;
    int l = run;
    while(s[run] != ':') {
        ++run;
    }
    return s.substr(l, run - l);
}
void Setup() {
    ifstream fp;
    fp.open("shadow");

    string s;
    while(getline(fp, s)) {
        v.push_back(s);
        if(un == s.substr(0, un.size())) {
            ep = takeEP(s);
            thes = s;
            // cout << "---" << thes;
            // cout << un << '\n';
            // cout << thes << '\n';
            // cout << ep << '\n';           
        }

    }
    fp.close();
}

void changePass() {
    thenews = thes;
    // cout << thenews << '\n';
    int run = 0;
    while(thenews[run] != ':') ++run;
    ++run;
    int l = run;
    while(thenews[run] != ':') {
        ++run;
    }
    thenews.erase(l, run - l);
    thenews.insert(l, nep);

    // cout << thenews << '\n';
    for(string &t : v) {
        if(t == thes) {
            // cout << t << '\n';
            t = thenews;
            // cout << t << '\n';
        }

    }
    // ofstream f;
    // f.open("shadow", ios::out | ios::app);
    // f.open("shadow", ios::trunc);
    freopen("shadow", "w", stdout);
    // cout << "1asdasdasd\n";
    for(string t : v) {
        // f << t << '\n';
        cout << t << '\n';
    }
    // f.close();
}

int main(int argc, char** argv){
    if (argc > 1 && std::string(argv[1]) == "-xterm") {
        if (::execl("/usr/bin/xterm", "xterm", "-e", argv[0], (char*)NULL)) {
      std::perror("execl");
      return 1;
        }
    }
    un = execute_command("whoami");
    un = std::regex_replace(un, std::regex("\\s"), "");
    // cout << un;
    cout << "Nhap mat khau cu: ";
    Setup();
    // cout << ep;
    cin >> p;
    char pp[p.size()+1];
    strcpy(pp, p.c_str());
    char epp[ep.size()+1];
    strcpy(epp, ep.c_str());
    auto tmp = crypt(pp, epp);
    if(tmp == ep) {
	string np;
        cout << "Nhap mat khau moi: ";
	    cin >> np;
        
        char npp[np.size()+1];
        strcpy(npp, np.c_str());
        nep = crypt(npp, epp);
        changePass();
    } else {
	   cout << "Mat khau khong chinh xac!!!\n";
    }
    return 0;
}
