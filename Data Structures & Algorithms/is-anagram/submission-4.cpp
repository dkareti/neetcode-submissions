class Solution {
public:

struct Node{

    int frequency = 0;
};
    bool isAnagram(string s, string t) {
        //Declare a count storage for string s
    unordered_map<char, Node> freq1; 
    unordered_map<char, Node> freq2;

    
    for(int i = 0; i < s.size(); ++i){
        freq1[s[i]].frequency += 1;
    }

    for(int j = 0; j < t.size(); ++j){
        freq2[t[j]].frequency += 1;
    }



    if(s.size() == t.size()){
        for(int i = 0; i < s.size(); ++i){
            if(freq1[s[i]].frequency != freq2[s[i]].frequency){
                return false;
            }
        }
        return true;
    }
    else{
        return false;
    }
    }
};
