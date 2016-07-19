class Solution(object):
    def romanToInt(self, s):
        
        myDict={"I":1,"IV":4,"V":5,"IX":9,"X":10,"XL":40,"L":50,"XC":90,"C":100,"CD":400,"D":500,"CM":900,"M":1000}
        length=len(s)
        
        left=0
        num=0
        while left<length:
            if left+1<length and myDict.has_key(s[left:left+2]):
                num+=myDict.get(s[left:left+2])
                left=left+2
            else:
                num=num+myDict.get(s[left:left+1])
                left+=1
        return num
