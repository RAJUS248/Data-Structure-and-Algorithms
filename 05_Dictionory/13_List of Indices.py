def get_indices(data):
    seen = {}
    data = data.lower()
    for i,value in enumerate(data):
            
            if value not in seen:
                seen[value] = []
            seen[value].append(i)

    return seen
data = "Bbanana"
print(get_indices(data))

# or

from collections import defaultdict

def get_indices_v2(data):

    data = data.lower()
    seen = defaultdict(list)

    for i,value in enumerate(data):
            seen[value].append(i)

    return dict(seen)
data = "Bbanana"
print(get_indices_v2(data))





