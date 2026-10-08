class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) 
    {
        vector<vector<string>>res;
        unordered_map<string,vector<string>>mp;


        /*
        key:排序后的样子
        value:每一个遍历到的元素
        */
        for(auto str:strs)
        {
            string key = str;
            sort(key.begin(),key.end());
            mp[key].push_back(str);
        }


        //开始恢复
        for(auto it = mp.begin();it != mp.end();it++)
        {
            res.push_back(it->second);
        }

        return res;
        
    }
};