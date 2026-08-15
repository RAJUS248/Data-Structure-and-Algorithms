"""
Example - 2:
Input:
5
-120-25
Output:
10
Constraints:
•1≤N≤2x 106
•1 ≤Ai] ≤ 1010
swered 1
Please type your code here in C langauge 03 [3 Not
Visited
The input format for testing:
The first line represents the N i.e., Number of elements in an array.
The second line represents the N elements, where the ith element consists of ith person's eneray.
The Output format for testing:
• Print the maximum energy possible for the last person.
"""

def find_energy(persons):

    total = persons[0]

    for i in range(1,len(persons)):
        total -= persons[i]

    return abs(total)

persons = [-1,2,0,-2,5]
print(find_energy(persons))