class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_memo = {}
        t_memo = {}

        for i in s:
            pre = s_memo.get(i, 0)
            s_memo[i] = pre + 1
        
        for j in t:
            if j not in s_memo.keys():
                return False
            pre = t_memo.get(j, 0)
            t_memo[j] = pre + 1

        for i in t:
            if s_memo[i] != t_memo[i]:
                return False
        return True