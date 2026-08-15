def fill_defaults(data, defaults):

    for key, value in defaults.items():
        data.setdefault(key, value) 

    return data

data = {"user": "Alice", "city": "NYC"}
defaults = {"city": "London", "country": "UK", "status": "Active"}
print(fill_defaults(data, defaults))