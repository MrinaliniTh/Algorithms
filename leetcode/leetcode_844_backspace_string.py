# Using Stack
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []
        for st in s:
            if st == "#":
                if s_stack:
                    s_stack.pop()
            else:
                s_stack.append(st)
        for ts in t:
            if ts == "#":
                if t_stack:
                    t_stack.pop()
            else:
                t_stack.append(ts)
        return s_stack == t_stack

# Using String manipulation
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_string = self.compare_string(s)
        t_string = self.compare_string(t)
        return s_string == t_string
    
    def compare_string(self, str):
        final_string = ""
        for s in str:
            if s == "#":
                final_string = final_string[:-1]
            else:
                final_string += s
        return final_string
            
                