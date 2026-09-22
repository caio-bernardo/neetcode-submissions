class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mirror = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for c in s:
            if c in mirror.keys():
                stack.append(c)
            else:
                if len(stack) > 0 and c == mirror[stack[-1]]:
                    stack.pop()
                else:
                    print(stack)
                    return False
        return len(stack) == 0