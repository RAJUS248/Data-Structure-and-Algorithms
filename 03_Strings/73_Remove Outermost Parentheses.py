def removeOuterParentheses(s):
        
        stack = []
        close = []
        res = ""
        for b in s:

            if b == ")" :

                par = stack.pop()
                
                if stack and len(stack) > 1:
                    res += par
                    close.append(b)
                    
                    

                elif stack:
                    res += par
                    res += b
                    
                    if close:
                        res += close.pop()

                

            else:
                stack.append(b)

        return res

s =  "((()())(()()))" # "(((((())))))" # "(()())(())(()(()))" # "(()())(())"
print(removeOuterParentheses(s))