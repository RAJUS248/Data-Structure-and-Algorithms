def rotateString(s, goal):
    
    if len(s) != len(goal):
        return False
    
    if s == goal:
        return True
    
    conc_str = s + s

    if goal in conc_str:
        return True
    
    else:
        return False

s = "abcde"
goal = "cdeab"
print(rotateString(s,goal))



# or

def rotateString_v2(s, goal):
    return len(s) == len(goal) and goal in (s + s)

s = "abcde"
goal = "cdeab"
print(rotateString_v2(s,goal))

