def isValid(s):
        
        stack = []

        mapping = {")":"(" , "}":"{" , "]":"["}

        for ch in s:

            if ch in mapping:

                top = stack.pop() if stack else "#"

                if mapping[ch] != top:
                    return False
                    
            # if ch in mapping:
            #     if not stack or stack.pop() != mapping[ch]:
            #         return False

            else:
                stack.append(ch)

        return len(stack) == 0

s = "()"
print(isValid(s))