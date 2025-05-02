class Solution:
    def isValid(self, s: str) -> bool:

        openset = {'{', '[', '('}
        hashmap = {'}': '{', ']': '[', ')': '('}

        if len(s) <= 1:
            return False
        stack = []
        for v, i in enumerate(s):
            if i in openset:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if stack[-1] != hashmap[i]:
                    return False
                else:
                    stack.pop()
        return True if len(stack) == 0 else False
