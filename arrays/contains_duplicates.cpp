/*
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false
Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
*/

#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>

using namespace std;

// Attempt #1: Using an unordered set

// class Solution {
// public:
//     bool hasDuplicate(vector<int>& nums) {
//         unordered_set<int> sample(nums.begin(), nums.end());
//         return !(nums.size() == sample.size());
//     }
// };

//Attempt 2: O(1) space complexity

class Solution {
    public:
        bool hasDuplicate(vector<int>& nums) {
            sort(nums.begin(), nums.end());

            for (int i = 0; i < nums.size()-1; i++) {
                if (nums[i] == nums[i+1]) {
                    return true;
                }
            }

            return false;
        }
    
};


int main() {
    Solution solution;
    vector<int> v = {1, 2, 3, 4, 5};
    cout << solution.hasDuplicate(v) << endl;
    return 0;
}