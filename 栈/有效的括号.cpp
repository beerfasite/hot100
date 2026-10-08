#include <stack>
#include <string>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        
        for(auto c : s)
        {
            if(c == '(' || c == '[' || c == '{')
            {
                st.push(c);
            }
            else
            {
                if(st.empty()) return false;
                char tt = st.top();
                if(tt == '(' && c == ')')
                {
                    st.pop();
                }
                else if(tt == '[' && c == ']')
                {
                    st.pop();
                }
                else if(tt == '{' && c == '}')
                {
                    st.pop();
                }
                else
                {
                    return false;
                }
            }
        }
        return st.empty();
    }
};
