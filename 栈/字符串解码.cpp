#include <stack>
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    string decodeString(string s) {
        stack<char> st;
        string res = "";
        for(auto c : s)
        {
            if(c != ']')
            {
                st.push(c);
            }
            else
            {
                string tmp = "";
                // 取出括号里面的字符
                while(st.top() != '[')
                {
                    char cc = st.top();
                    tmp += cc;
                    st.pop();
                }
                st.pop(); // 弹出 '['

                // ==========修复1：读取多位数cnt（你原来的cnt变量）==========
                string numStr;
                while(!st.empty() && isdigit(st.top()))
                {
                    numStr += st.top();
                    st.pop();
                }
                reverse(numStr.begin(), numStr.end());
                int cnt = stoi(numStr);

                reverse(tmp.begin(), tmp.end());
                // 重复 cnt 次压回栈
                for(int i = 0; i < cnt; i++)
                {
                    for(auto x : tmp)
                    {
                        st.push(x);
                    }
                }
            }
        }
        // ==========修复2：stack不能for遍历，改用top+pop收集res==========
        while(!st.empty())
        {
            res += st.top();
            st.pop();
        }
        reverse(res.begin(), res.end());
        return res;
    }
};
