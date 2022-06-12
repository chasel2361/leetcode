class Solution {
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {
        unordered_map<string, int> words;
        // clean paragraph
        for(int i=0; i<paragraph.size();){
            string s = "";
            while(i < paragraph.size() && isalpha(paragraph[i])){
                s.push_back(tolower(paragraph[i++]));
            }
            while(i < paragraph.size() && !isalpha(paragraph[i])){
                i++;
            }
            // count a word
            words[s]++;
        }
        for(auto x: banned) words[x] = 0;
        string res = "";
        int count = 0;
        // choose max count
        for(auto x: words){
            if(x.second > count){
                res = x.first;
                count = x.second;
            }
        }
        return res;
    }
};