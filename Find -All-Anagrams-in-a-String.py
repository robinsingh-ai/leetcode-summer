from collections import Counter

def findAnagrams(s: str, p: str) -> List[int]:
    if len(p) > len(s):
        return []

    pCount, sCount = Counter(p), Counter(s[:len(p)-1])
    result = []
    
    for i in range(len(p) - 1, len(s)):
        sCount[s[i]] += 1   # Add the new character to the window
        if sCount == pCount:
            result.append(i - len(p) + 1)  # Found an anagram
        
        sCount[s[i - len(p) + 1]] -= 1  # Remove the character left out of the window
        if sCount[s[i - len(p) + 1]] == 0:
            del sCount[s[i - len(p) + 1]]  # Remove the count entry if it's zero to maintain the correct size of the counter

    return result