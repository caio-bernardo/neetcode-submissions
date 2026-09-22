class Solution:
    # Encode language
    # for each string
    # append count and su
    #
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s + '#'
        return res

    def decode(self, s: str) -> List[str]:
        # read chars until the #
        # if digit mode, set digit
        # if string mode, add to answer increment counter
        # if string read is equal to length
        # switch mode
        res = []
        mode = "length" # length mode | string mode
        buf = ""
        size = 0
        for c in s:
            if c == '#' and mode == "length":
                size = int(buf)
                buf = ""
                mode = "string"
                continue
            if c == '#' and mode == "string" and len(buf) == size:
                res.append(buf)
                buf = ""
                size = 0
                mode = "length"
                continue
            buf += c
        return res

        