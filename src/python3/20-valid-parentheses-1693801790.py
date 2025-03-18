class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = tuple('({[')
        close_brackets = tuple(')}]')
        brackets_dict = dict(zip(open_brackets, close_brackets))
        stack = []
        
        for bracket in s:
            if bracket in open_brackets:
                stack.append(brackets_dict[bracket])
            elif bracket in close_brackets:
                if not stack or bracket != stack.pop():
                    return False
        if not stack:
            return True
        else:
            return False
