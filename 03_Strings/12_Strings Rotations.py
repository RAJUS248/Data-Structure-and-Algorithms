def are_rotations(s1,s2):

    temp = s1 + s1

    return s2 in temp

s1 = "abcd"
s2 = "cdab"

print(are_rotations(s1,s2))