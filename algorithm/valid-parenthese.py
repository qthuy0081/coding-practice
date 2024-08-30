class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        stack = []
        for i in range(len(s)):
            if s[i] in parentheses:
                stack.append(s[i])
            elif len(stack) == 0 or parentheses.get(stack.pop()) != s[i]:
                return False
        return len(stack) == 0
    
def test_isValid():
    solution = Solution()
    
    assert solution.isValid("()") == True
    assert solution.isValid("()[]{}") == True
    assert solution.isValid("(]") == False
    assert solution.isValid("([)]") == False
    assert solution.isValid("{[]}") == True
    assert solution.isValid("") == True
    assert solution.isValid("((") == False
    
    print("All tests passed!")

# Run the tests
test_isValid()