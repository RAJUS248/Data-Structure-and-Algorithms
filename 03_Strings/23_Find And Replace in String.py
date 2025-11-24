def find_replace(s,indices,sources,targets):

    lookup = {}

    for i,src,tgt in zip(indices,sources,targets):

        if s[i:i+len(src)] == src:
            lookup[i] = (src,tgt)

    res = []
    i = 0

    while i < len(s):

        if i in lookup:

            src,tgt = lookup[i]

            res.append(tgt)

            i += len(src)

        else:
            res.append(s[i])

            i += 1

    return "".join(res)


s = "abcd" 
indices = [0, 2] 
sources = ["ab","ec"]
targets = ["eee","ffff"]
print(find_replace(s,indices,sources,targets))