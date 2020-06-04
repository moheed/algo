class Solution:
    #c1 is always opening type
    def counter_part(self, c1: str, c2:str)->bool:
        if c1  == '(' and c2 == ')':
            return True
        if c1  == '{' and c2 == '}':
            return True
        if c1  == '[' and c2 == ']':
            return True
        return False
    
    def isValid(self, s: str) -> bool:
        stack=[]
        opening_type=['(', '{', '[']
        closing_type=[')', '}', ']']
        for x in s:
            if x in opening_type:
                print("here")
                stack.append(x)
            if x in closing_type:
                try:
                    c=stack.pop()
                    if self.counter_part(c, x):
                        #we good, continue with next char in i/p string
                        print("here2", c, x)
                        continue
                    else:
                        #we dont have a matched
                        print("here3",x, c)
                        return False
                except IndexError:#we found a closing type, but nothing left in stack
                    return False
        try:
            stack.pop()
            return False
        except IndexError:
            return True
