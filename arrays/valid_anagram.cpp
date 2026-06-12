/*
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.
*/

#include <iostream>
#include <string>
#include <array>

using namespace std;

// Attempt 1: Using an array bucket

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }

        array<int, 26> bucket{};

        for (size_t i = 0; i < s.size(); i++) {
            bucket[s[i] - 'a'] += 1;
            bucket[t[i] - 'a'] -= 1;
        }

        for (int val : bucket) {
            if (val != 0) {
                return false;
            }
        }

        return true;
    }
};

int main() {
    Solution solution;
    
    string s, t;
    s="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab";
    t="bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbba";

    cout << "Is this an anagram: " << solution.isAnagram(s, t) << endl;


    // array<int, 26> bucket{};

    // for (int i: bucket) {
    //     cout << "Element: " << i << endl;
    // }

    return 0;
}