"""
1249. Minimum Remove to Make Valid Parentheses
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
 

Constraints:

1 <= s.length <= 105
s[i] is either '(' , ')', or lowercase English letter.

Intuition - use count to keep track of open and close paranthesis, 
if there exists a value for count even after iterating through the string, 
then we need to remove the extra paranthesis without going thru the whole array again.
"""

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        count = 0

        for ch in s:
            if ch == "(":
                res.append(ch)
                count += 1
            elif ch == ")" and count > 0:
                count -= 1
                res.append(ch)
            elif ch != ")":
                res.append(ch)

        i = len(res) - 1
        while count > 0 and i >= 0 :
            if res[i] == "(":
                res[i] = ""
                count -= 1
            i -= 1

        return "".join(res)