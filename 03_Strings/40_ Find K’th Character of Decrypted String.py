def kThCharaterOfDecryptedString(s, k):

    i = 0
    n = len(s)

    cur_len = 0

    while i < n:
        sub_str = ''

        while i < n and s[i].isalpha():
            sub_str += s[i]
            i += 1

        
        num_str = ''

        while i < n and s[i].isdigit():
            num_str += s[i]
            i += 1

        count = int(num_str)

        chunk_len = len(sub_str) * count

        if k <= cur_len + chunk_len:

            remain_k = k - cur_len

            char_idx = (remain_k - 1) % len(sub_str)

            return sub_str[char_idx]
        
        cur_len += chunk_len


    return ""


s = "dajidas988ksajlkdn908"
k = 900
print(kThCharaterOfDecryptedString(s,k))