class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        parentheses = []

        def backtrack(opened, closed):
            if opened == closed == n:
                parentheses.append(''.join(stack))
                return
            
            if opened < n:
                stack.append('(')
                backtrack(opened+1, closed)
                stack.pop()
            
            if closed < opened:
                stack.append(')')
                backtrack(opened, closed+1)
                stack.pop()
        
        backtrack(0, 0)
        return parentheses
