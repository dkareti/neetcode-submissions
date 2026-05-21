class Solution {
public:
    bool isAnagram(string s, string t) {
        //Declare a count storage for string s
    int sum1 = 0;

    //Declare a count storage for string t
    int sum2 = 0;
    if(s.size() == t.size()){
        //The loop can refer to string s or t, because anagrams means they are of the same length
        for (int i = 0; i < s.size(); ++i){
            sum1 += int(s[i]);
            sum2 += int(t[i]);
        }
        if(sum1 == sum2){
            return true;
        }
    }
    

    
    return false;
    
    }
};
