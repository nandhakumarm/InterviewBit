class Solution(object):
    def isNumber(self, s):
        
        try:
            if s[len(s)-1]==".":
                return 0
            temp=s.find(".")
            if temp!=-1:
                if s[temp+1].isdigit()==False:
                    return 0
            float(s)
            return 1
        except ValueError:
            return 0
