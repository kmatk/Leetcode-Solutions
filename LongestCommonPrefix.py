# Variables for testing 
test1 = ["flower", "flow", "flight"]
test2 = ["tacks", "flower", "door"]
test3 = ["trust", "trumpet", "truck"]
test4 = ["a"]
test5 = [""]
test6 = ["flower", "flower", "flower"]

def longestCommonPrefix(strs) -> str:
    # Store lenght of the shortest string provided
    shortest = len(min(strs, key=len))
    
    # Check to see if any strings are empty, if so, return ""
    for word in strs:
        if word == "":
            return ""
    
    # Store the first character of the first string in prefix, create prevPrefix to store info for next iteration
    prefix = strs[0][0]
    prevPrefix = ""
    
    # Iterate through words in the list, letter by letter. IE word #1 letter #1, word #2 letter #1, etc..
    for i in range(1, shortest+1):
        # Store the first i letters in variable prefix
        prefix = strs[0][:i]
        print(prefix)
        
        # Iterate through words to evaluate if the first i letters match those in the first word
        # If they don't, we know the previous prefix (prevPrefix) was the longest prefix
        for word in strs:
            if word[:i] != prefix:
                return prevPrefix
        
        # Store prefix in prevPrefix to be recalled if next prefix doesn't match all words
        prevPrefix = prefix
                
    return prefix

# Testing
print("----")
print(longestCommonPrefix(test1))
print("----")
print(longestCommonPrefix(test2))
print("----")
print(longestCommonPrefix(test3))
print("----")
print(longestCommonPrefix(test4))
print("----")
print(longestCommonPrefix(test5))
print("----")
print(longestCommonPrefix(test6))
print("----")