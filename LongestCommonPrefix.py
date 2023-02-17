"""
[Insert problem logic here]
"""
test1 = ["flower", "flow", "flight", "trust", "tower", "tail", "stray"]
test2 = ["tacks", "flower", "door", "strobe"]
def longestCommonPrefix(strs) -> str:
    # Find the longest word in the provided list
    longest = max(strs, key=len)
    prefixes = {}
    
    for word in strs:
        if word[0] not in prefixes:
            prefixes[word[0]] = 1
        else:
            prefixes[word[0]] += 1
    # If len(strs) = len(prefixes) that means all first letters are unique, therefore we return an empty String
    if len(strs) == len(prefixes):
        return ""
    
    # Loop through subsequent letters of the list
    currPrefixes = prefixes
    nextPrefixes = {}
    for i in range(1, len(longest)):
        print(strs)
        for ix, word in enumerate(strs):
            if word[:i] not in currPrefixes:
                strs.pop(ix)
            print(ix)
            print(word[:ix])
            print(strs)