def swap_dict(original_dict):
    seen = {}
    for key, value in original_dict.items():
        seen[value] = key
    
    return seen

original_dict = {"name": "Alice", "role": "Engineer", "dept": "R&D"}
print(swap_dict(original_dict))

# or

def swap_dict_v2(original_dict):
    # The curly braces { ... } *always* define and create a BRAND NEW dictionary object.
    return {value: key for key, value in original_dict.items()}

original_dict = {"name": "Alice", "role": "Engineer", "dept": "R&D"}
print(swap_dict_v2(original_dict))

