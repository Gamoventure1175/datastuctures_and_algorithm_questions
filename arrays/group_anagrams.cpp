/*
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
Example 2:

Input: strs = ["x"]

Output: [["x"]]
Example 3:

Input: strs = [""]

Output: [[""]]
Constraints:

1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.
*/

// Attempt 1: Using a fucking map

#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>
#include <array>

using namespace std;

class Solution {
public:
    string characters(const string& s) {
        array<int,26> bucket= {};

        for (const auto& ele : s) {
            bucket[ele - 'a']++;
        }

        string result = "";

        for (const auto& ele : bucket) {
            result += to_string(ele);
            result += "#";
        }

        return result;
    } 

    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> anagramGroups;

        for (const auto& str : strs) {
            auto charCount = characters(str);
            anagramGroups[charCount].push_back(str);
        }

        vector<vector<string>> result;
        for (const auto& group : anagramGroups) {
            result.push_back(group.second);
        }

        return result;
    }
};


int main() {
    Solution solution = Solution();

    string sample = "gaurav";

    auto result = solution.characters(sample);

    cout << result << endl;

    return 0;
}