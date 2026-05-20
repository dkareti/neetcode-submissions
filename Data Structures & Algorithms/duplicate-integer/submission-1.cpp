class Solution {


public:

struct Node{
    int value = 0;
};

    bool hasDuplicate(vector<int>& nums) {
            unordered_map<int, Node> counter;

        //Assume that all the values in the nums array are ints
        for(int i = 0; i < nums.size(); ++i){
            if(counter[nums[i]].value != 0){
                return true;
            }
            counter[nums[i]].value += 1;
        }
        return false;

        return 0;



    }
};
