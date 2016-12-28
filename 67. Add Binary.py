#   Question: 67. Add Binary
# Difficulty: Easy
#       Tags: Math, String
'''
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

'''
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a,2)+int(b,2))[2:]
