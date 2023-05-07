# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

def longest_common_prefix(strs):
    if not strs:  # If the input list is empty
        return ""
    
    # Find the minimum length among the strings
    min_length = min(len(s) for s in strs)
    
    # Iterate over the characters at each position
    for i in range(min_length):
        char = strs[0][i]  # Take the character from the first string
        
        # Check if the character matches in all strings
        if all(s[i] == char for s in strs):
            continue  # Continue to the next character
        else:
            return strs[0][:i]  # Return the common prefix until this point
    
    return strs[0][:min_length]  # All characters matched, return the common prefix

# Testing the function
print(longest_common_prefix(["flower", "flow", "flight"]))  # Output: "fl"
print(longest_common_prefix(["dog", "racecar", "car"]))  # Output: ""
