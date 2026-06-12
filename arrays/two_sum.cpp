/*
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

*/

#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

// Attempt 1: Using a hashmap maybe?

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> umap;
        
        for (size_t i = 0; i < nums.size(); i++ ) {
            const int complement = target - nums[i];
            auto found = umap.find(complement);

            if (found != umap.end()) {
                return {found->second, (int) i};

            } else {
                umap[nums[i]] = i;
            }
        }

        return {-1, -1};
    }
};

int main() {
    Solution slu;
    vector<int> nums = {3, 2, 4};
    int target = 6;
    vector<int> answer = slu.twoSum(nums, target);

    cout << "Solution: " << endl;
    for (int i : answer) {
        cout << i << endl;
    }
    
    return 0;
}