class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = {}
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            if s[right] in charMap and charMap[s[right]] >= left:
                left = charMap[s[right]] + 1
            
            charMap[s[right]] = right
            max_length = max(max_length, right - left + 1)
        
        return max_length
    
print(Solution().lengthOfLongestSubstring("abcabcbb"))