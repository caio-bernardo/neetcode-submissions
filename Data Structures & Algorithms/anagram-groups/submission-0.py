class Solution:
    # t: O(n * m) E: O(n)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            freqs = [0] * 26
            for c in s:
                freqs[ord(c) - ord('a')] = freqs[ord(c) - ord('a')] + 1
            groups[hash(tuple(freqs))] = groups.get(hash(tuple(freqs)), []) + [s]

        return list(groups.values())
