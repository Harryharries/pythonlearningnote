def lengthOfLongestSubstring(s):
    seen = {}
    current_max = result = 0
    for i, c in enumerate(s):
        if c not in seen or seen[c]<(i-current_max):
            seen[c] = i
            current_max += 1
        else:
            current_max = i - seen[c]
            seen[c] = i
        result = max(result, current_max)
    return result

print(lengthOfLongestSubstring("abba"))