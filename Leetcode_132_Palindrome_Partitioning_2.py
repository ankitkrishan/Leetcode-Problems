def solve(s: str, mp):
    if s == "":
        return 1000000
    if s[::-1] == s:
        return 0
    currentKey = s
    if currentKey in mp:
        return mp[currentKey]
    ans = 1000000
    for i in range(1, len(s)):
        cut = 1000000
        if s[:i][::-1] == s[:i]:
            cut =  1 + solve(s[i:], mp)
        ans = min(cut, ans)
    mp[currentKey] = ans
    return mp[currentKey]
class Solution:
    def minCut(self, s: str):
        if s[::-1] == s:
            return 0
        return solve(s, {})
