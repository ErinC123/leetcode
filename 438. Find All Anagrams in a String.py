#   Question: 438. Find All Anagrams in a String
# Difficulty: Easy
#       Tags: Hash Table
'''
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger
than 20,100.

The order of output does not matter.

Example 1:
Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''

from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []
        pdic = Counter(p)
        sdic = Counter(s[:len(p)-1])
        for i in range(len(p)-1, len(s)):
            sdic[s[i]] = sdic.get(s[i], 0) + 1
            if sdic == pdic:
                result.append(i-len(p)+1)
            sdic[s[i-len(p)+1]] -= 1
            if sdic[s[i-len(p)+1]] == 0:
                del sdic[s[i-len(p)+1]]
        return result